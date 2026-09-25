# Decision Report

- generated_at: 2026-09-25T19:11:24.532897+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15538**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=15538, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=-2.47%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.47% | **-2.47%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT | 16/20 | 80.0% | +1.01% | **+0.81%** |
| LIMIT_5PCT | 2/20 | 10.0% | +4.48% | **+0.45%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +1.38% | **+0.34%** |
| LIMIT_3PCT | 16/20 | 80.0% | +0.16% | **+0.13%** |
| LIMIT_ATR | 18/20 | 90.0% | -0.25% | **-0.23%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +2.29% | **+1.49%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | +2.17% | **+1.19%** |
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +1.48% | **+1.11%** |
| LIMIT_4PCT_LONG | 8/20 | 40.0% | +2.73% | **+1.09%** |
| LIMIT_3PCT_LONG | 9/20 | 45.0% | +2.24% | **+1.01%** |

## 2. $100 Live Portfolio

- 残高: **$120.55** / 初期 $100.00 (+20.55%)
- 確定トレード: 222件 (TP 81 / SL 135 / EXP 6)
- 最新: APT/USDT:USDT EXPIRED PnL -0.12% 残高後 $120.55
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,207.62** / 初期 $100.00 (+1107.62%)
- 確定: 5903件 (Win 1741 / Loss 1891 / Flat 2271) / skip 6196件
- 成長率目線: 平均log +0.000422 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: NEAR/USDT:USDT `LIMIT_BB3S_LONG` EXPIRED account +0.56% 残高後 $1,207.62

## 4. Robust Adaptive DryRun ($100)

- 残高: **$256.32** / 初期 $100.00 (+156.32%)
- 確定: 3471件 (Win 952 / Loss 793 / Flat 1726) / skip 5478件
- 成長率目線: 平均log +0.000271 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0248 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: MUBARAK/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $256.32

## 5. Causal Adaptive DryRun ($100)

- 残高: **$119.91** / 初期 $100.00 (+19.91%)
- 確定: 3171件 (Win 933 / Loss 1255 / Flat 983) / pending 1件 / skip 3839件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000235 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: XPL/USDT:USDT `MARKET` EXPIRED account -0.07% 残高後 $119.91

## 6. Latest Market Context

- 更新: 2026-09-25T19:11:11.874057+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.02% price=83910.9
- Funnel: target 1067 → liquid 167 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LYN/USDT:USDT | +35.37% | $5,605,331.75 |
| PHA/USDT:USDT | +14.56% | $14,676,406.68 |
| GRASS/USDT:USDT | +12.59% | $2,147,198.28 |
| BR/USDT:USDT | +11.96% | $8,677,644.30 |
| BP/USDT:USDT | +9.91% | $1,112,889.01 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BP/USDT:USDT | below_1h_threshold | +4.77% | +4.79% |
| BR/USDT:USDT | below_1h_threshold | +3.16% | +3.18% |
| MUBARAK/USDT:USDT | below_1h_threshold | +2.20% | +2.22% |
| JTO/USDT:USDT | below_1h_threshold | +1.79% | +1.82% |
| PHA/USDT:USDT | below_1h_threshold | +1.69% | +1.71% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
