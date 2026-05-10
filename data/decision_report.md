# Decision Report

- generated_at: 2026-05-10T19:07:44.781328+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3983**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3983, expectancy=-0.13%
- 直近20件 MARKET基準: n=20, expectancy=-0.92%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.92% | **-0.92%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 9/20 | 45.0% | +0.42% | **+0.19%** |
| LIMIT_5PCT | 4/20 | 20.0% | +0.95% | **+0.19%** |
| LIMIT_4PCT | 12/20 | 60.0% | +0.05% | **+0.03%** |
| LIMIT_BB3S | 4/13 | 30.8% | -0.80% | **-0.25%** |
| LIMIT_3PCT | 14/20 | 70.0% | -0.44% | **-0.31%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +1.39% | **+1.11%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +1.47% | **+0.96%** |
| MARKET_LONG | 20/20 | 100.0% | +0.87% | **+0.87%** |
| ASK_LONG | 20/20 | 100.0% | +0.84% | **+0.84%** |
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +1.69% | **+0.68%** |

## 2. $100 Live Portfolio

- 残高: **$98.21** / 初期 $100.00 (-1.79%)
- 確定トレード: 30件 (TP 7 / SL 20 / EXP 3)
- 最新: SATO/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.21
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$107.73** / 初期 $100.00 (+7.73%)
- 確定: 198件 (Win 48 / Loss 66 / Flat 84) / skip 346件
- 成長率目線: 平均log +0.000376 / 幾何平均 +0.038% per trade / maxDD +4.09%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BILL/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account +0.00% 残高後 $107.73

## 4. Latest Market Context

- 更新: 2026-05-10T19:07:41.731599+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.04% price=81202.7
- Funnel: target 769 → liquid 164 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ALCH/USDT:USDT | +21.01% | $2,194,501.75 |
| TROLLSOL/USDT:USDT | +16.88% | $3,495,497.06 |
| B/USDT:USDT | +15.81% | $1,934,490.36 |
| SUI/USDT:USDT | +12.24% | $558,890,183.61 |
| TRUTH/USDT:USDT | +11.99% | $2,342,493.18 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TROLLSOL/USDT:USDT | below_1h_threshold | +4.54% | +4.58% |
| B/USDT:USDT | below_1h_threshold | +1.39% | +1.43% |
| BSB/USDT:USDT | below_1h_threshold | +0.94% | +0.98% |
| INX/USDT:USDT | below_1h_threshold | +0.76% | +0.80% |
| TRIA/USDT:USDT | below_1h_threshold | +0.68% | +0.72% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
