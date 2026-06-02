# Decision Report

- generated_at: 2026-06-02T09:19:33.255291+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5438**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=5438, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=+0.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.20% | **+0.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 6/20 | 30.0% | +1.30% | **+0.39%** |
| ASK | 20/20 | 100.0% | +0.29% | **+0.29%** |
| LIMIT_2PCT | 16/20 | 80.0% | +0.27% | **+0.22%** |
| LIMIT_4PCT | 13/20 | 65.0% | +0.31% | **+0.20%** |
| MARKET | 20/20 | 100.0% | +0.20% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +0.61% | **+0.42%** |
| LIMIT_10PCT_LONG | 6/20 | 30.0% | +1.11% | **+0.33%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +0.49% | **+0.32%** |
| MARKET_LONG | 20/20 | 100.0% | +0.20% | **+0.20%** |
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +0.15% | **+0.07%** |

## 2. $100 Live Portfolio

- 残高: **$96.14** / 初期 $100.00 (-3.86%)
- 確定トレード: 85件 (TP 24 / SL 58 / EXP 3)
- 最新: ESPORTS/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.14
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$133.62** / 初期 $100.00 (+33.62%)
- 確定: 950件 (Win 223 / Loss 286 / Flat 441) / skip 1049件
- 成長率目線: 平均log +0.000305 / 幾何平均 +0.031% per trade / maxDD +7.25%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: EPIC/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $133.62

## 4. Latest Market Context

- 更新: 2026-06-02T09:19:30.672537+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.29% price=69587.2
- Funnel: target 772 → liquid 151 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| US/USDT:USDT | +37.35% | $2,163,294.96 |
| MRVLSTOCK/USDT:USDT | +27.23% | $3,773,605.38 |
| USELESS/USDT:USDT | +22.02% | $1,700,724.77 |
| LAB/USDT:USDT | +19.69% | $212,093,431.64 |
| RIF/USDT:USDT | +19.60% | $1,876,497.15 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| STG/USDT:USDT | below_1h_threshold | +4.48% | +4.77% |
| PIEVERSE/USDT:USDT | below_1h_threshold | +3.46% | +3.75% |
| LAB/USDT:USDT | below_1h_threshold | +3.06% | +3.34% |
| EPIC/USDT:USDT | below_1h_threshold | +2.22% | +2.51% |
| INJ/USDT:USDT | below_1h_threshold | +0.98% | +1.27% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
