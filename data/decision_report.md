# Decision Report

- generated_at: 2026-09-25T20:21:26.834330+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15541**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=15541, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=-2.32%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.32% | **-2.32%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT | 15/20 | 75.0% | +0.54% | **+0.41%** |
| LIMIT_3PCT | 15/20 | 75.0% | +0.23% | **+0.18%** |
| LIMIT_5PCT | 2/20 | 10.0% | +0.95% | **+0.10%** |
| LIMIT_FIB1272 | 4/20 | 20.0% | -0.23% | **-0.05%** |
| LIMIT_ATR | 18/20 | 90.0% | -0.85% | **-0.76%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +3.06% | **+1.99%** |
| LIMIT_3PCT_LONG | 9/20 | 45.0% | +3.58% | **+1.61%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | +2.80% | **+1.54%** |
| LIMIT_4PCT_LONG | 6/20 | 30.0% | +4.13% | **+1.24%** |
| LIMIT_FIB1272_LONG | 7/20 | 35.0% | +3.32% | **+1.16%** |

## 2. $100 Live Portfolio

- 残高: **$120.55** / 初期 $100.00 (+20.55%)
- 確定トレード: 222件 (TP 81 / SL 135 / EXP 6)
- 最新: APT/USDT:USDT EXPIRED PnL -0.12% 残高後 $120.55
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,207.42** / 初期 $100.00 (+1107.42%)
- 確定: 5905件 (Win 1742 / Loss 1892 / Flat 2271) / skip 6197件
- 成長率目線: 平均log +0.000422 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: UNI/USDT:USDT `LIMIT_BB3S_LONG` EXPIRED account -0.23% 残高後 $1,207.42

## 4. Robust Adaptive DryRun ($100)

- 残高: **$256.50** / 初期 $100.00 (+156.50%)
- 確定: 3474件 (Win 953 / Loss 793 / Flat 1728) / skip 5478件
- 成長率目線: 平均log +0.000271 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0247 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: UNI/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $256.50

## 5. Causal Adaptive DryRun ($100)

- 残高: **$119.91** / 初期 $100.00 (+19.91%)
- 確定: 3171件 (Win 933 / Loss 1255 / Flat 983) / pending 3件 / skip 3839件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000260 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: XPL/USDT:USDT `MARKET` EXPIRED account -0.07% 残高後 $119.91

## 6. Latest Market Context

- 更新: 2026-09-25T20:21:16.607940+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.01% price=83963.4
- Funnel: target 1067 → liquid 168 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BR/USDT:USDT | +16.80% | $9,090,682.87 |
| PHA/USDT:USDT | +13.06% | $15,867,519.64 |
| LYN/USDT:USDT | +12.48% | $6,988,100.76 |
| SEI/USDT:USDT | +11.03% | $27,197,387.45 |
| BP/USDT:USDT | +11.02% | $1,168,702.36 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SEI/USDT:USDT | below_1h_threshold | +2.78% | +2.79% |
| GRT/USDT:USDT | below_1h_threshold | +2.52% | +2.53% |
| AVNT/USDT:USDT | below_1h_threshold | +2.23% | +2.24% |
| BR/USDT:USDT | below_1h_threshold | +2.04% | +2.05% |
| EIGEN/USDT:USDT | below_1h_threshold | +2.00% | +2.01% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
