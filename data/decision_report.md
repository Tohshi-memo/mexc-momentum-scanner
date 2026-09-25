# Decision Report

- generated_at: 2026-09-25T21:06:16.911458+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15542**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=15542, expectancy=+0.00%
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
| LIMIT_FIB1272 | 5/20 | 25.0% | -0.21% | **-0.05%** |
| LIMIT_ATR | 18/20 | 90.0% | -0.81% | **-0.73%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +3.06% | **+1.99%** |
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +3.95% | **+1.97%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +3.23% | **+1.94%** |
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +3.90% | **+1.56%** |
| LIMIT_4PCT_LONG | 6/20 | 30.0% | +4.13% | **+1.24%** |

## 2. $100 Live Portfolio

- 残高: **$120.55** / 初期 $100.00 (+20.55%)
- 確定トレード: 222件 (TP 81 / SL 135 / EXP 6)
- 最新: APT/USDT:USDT EXPIRED PnL -0.12% 残高後 $120.55
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,216.66** / 初期 $100.00 (+1116.66%)
- 確定: 5906件 (Win 1743 / Loss 1892 / Flat 2271) / skip 6197件
- 成長率目線: 平均log +0.000423 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BP/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.77% 残高後 $1,216.66

## 4. Robust Adaptive DryRun ($100)

- 残高: **$256.50** / 初期 $100.00 (+156.50%)
- 確定: 3475件 (Win 953 / Loss 793 / Flat 1729) / skip 5478件
- 成長率目線: 平均log +0.000271 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0223 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BP/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $256.50

## 5. Causal Adaptive DryRun ($100)

- 残高: **$120.22** / 初期 $100.00 (+20.22%)
- 確定: 3172件 (Win 934 / Loss 1255 / Flat 983) / pending 3件 / skip 3839件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000255 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BP/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.26% 残高後 $120.22

## 6. Latest Market Context

- 更新: 2026-09-25T21:06:08.856705+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.14% price=83723.9
- Funnel: target 1067 → liquid 169 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PHA/USDT:USDT | +15.34% | $17,183,422.36 |
| BR/USDT:USDT | +14.01% | $8,981,277.46 |
| BP/USDT:USDT | +10.76% | $1,218,130.41 |
| SEI/USDT:USDT | +8.54% | $30,995,475.86 |
| ONE/USDT:USDT | +7.09% | $8,384,669.34 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| MUBARAK/USDT:USDT | below_1h_threshold | +1.36% | +1.49% |
| ARK/USDT:USDT | below_1h_threshold | +0.70% | +0.84% |
| BP/USDT:USDT | below_1h_threshold | +0.42% | +0.55% |
| ONE/USDT:USDT | below_1h_threshold | +0.41% | +0.54% |
| CC/USDT:USDT | below_1h_threshold | +0.33% | +0.47% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
