# Decision Report

- generated_at: 2026-05-17T22:23:47.175043+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4422**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4422, expectancy=-0.09%
- 直近20件 MARKET基準: n=20, expectancy=-0.74%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.74% | **-0.74%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 5/20 | 25.0% | +1.89% | **+0.47%** |
| LIMIT_BB3S | 4/13 | 30.8% | +1.43% | **+0.44%** |
| LIMIT_5PCT | 5/20 | 25.0% | +0.95% | **+0.24%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | -0.30% | **-0.12%** |
| LIMIT_4PCT | 14/20 | 70.0% | -0.29% | **-0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +2.53% | **+1.65%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +2.21% | **+1.44%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +2.14% | **+1.39%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +1.44% | **+0.72%** |
| ASK_LONG | 20/20 | 100.0% | +0.64% | **+0.64%** |

## 2. $100 Live Portfolio

- 残高: **$96.71** / 初期 $100.00 (-3.29%)
- 確定トレード: 51件 (TP 13 / SL 35 / EXP 3)
- 最新: AIGENSYN/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.71
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$122.58** / 初期 $100.00 (+22.58%)
- 確定: 419件 (Win 110 / Loss 141 / Flat 168) / skip 564件
- 成長率目線: 平均log +0.000486 / 幾何平均 +0.049% per trade / maxDD +4.21%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BUILDONBOB/USDT:USDT `LIMIT_2PCT_LONG` TP_HIT account +1.00% 残高後 $122.58

## 4. Latest Market Context

- 更新: 2026-05-17T22:23:45.270808+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.48% price=77991.1
- Funnel: target 760 → liquid 121 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| FIDA/USDT:USDT | +19.36% | $2,907,909.95 |
| BUILDONBOB/USDT:USDT | +17.35% | $1,243,458.08 |
| UB/USDT:USDT | +11.62% | $14,138,810.47 |
| BILL/USDT:USDT | +7.80% | $34,316,878.98 |
| HYPE/USDT:USDT | +7.13% | $291,181,406.75 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| FIDA/USDT:USDT | below_1h_threshold | +1.33% | +1.81% |
| SILVER/USDT:USDT | below_1h_threshold | +0.99% | +1.47% |
| USOIL/USDT:USDT | below_1h_threshold | +0.83% | +1.31% |
| XPD/USDT:USDT | below_1h_threshold | +0.75% | +1.23% |
| NMR/USDT:USDT | below_1h_threshold | +0.47% | +0.94% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
