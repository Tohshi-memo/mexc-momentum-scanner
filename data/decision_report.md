# Decision Report

- generated_at: 2026-06-09T18:57:09.625227+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6156**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6156, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+0.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.20% | **+0.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT | 15/20 | 75.0% | +0.42% | **+0.32%** |
| ASK | 20/20 | 100.0% | +0.23% | **+0.23%** |
| MARKET | 20/20 | 100.0% | +0.20% | **+0.20%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +0.66% | **+0.07%** |
| LIMIT_6PCT | 3/20 | 15.0% | -0.08% | **-0.01%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 13/20 | 65.0% | +1.40% | **+0.91%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | +5.95% | **+0.89%** |
| LIMIT_5PCT_LONG | 12/20 | 60.0% | +1.14% | **+0.68%** |
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +1.00% | **+0.60%** |
| LIMIT_6PCT_LONG | 11/20 | 55.0% | +0.70% | **+0.39%** |

## 2. $100 Live Portfolio

- 残高: **$95.66** / 初期 $100.00 (-4.34%)
- 確定トレード: 13件 (TP 1 / SL 11 / EXP 1)
- 最新: PIPPIN/USDT:USDT SL_HIT PnL -4.00% 残高後 $95.66
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$148.01** / 初期 $100.00 (+48.01%)
- 確定: 1188件 (Win 297 / Loss 374 / Flat 517) / skip 1529件
- 成長率目線: 平均log +0.000330 / 幾何平均 +0.033% per trade / maxDD +7.25%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: EPIC/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $148.01

## 4. Latest Market Context

- 更新: 2026-06-09T18:57:06.807178+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.05% price=61694.3
- Funnel: target 778 → liquid 160 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ESPORTS/USDT:USDT | +17.32% | $22,107,972.58 |
| HOME/USDT:USDT | +15.74% | $3,793,456.16 |
| BTW/USDT:USDT | +11.26% | $4,768,328.99 |
| SENT/USDT:USDT | +8.87% | $1,316,110.88 |
| LIT/USDT:USDT | +8.43% | $3,241,457.73 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| HOME/USDT:USDT | below_1h_threshold | +4.56% | +4.51% |
| OPN/USDT:USDT | below_1h_threshold | +3.90% | +3.85% |
| BTW/USDT:USDT | below_1h_threshold | +2.65% | +2.60% |
| WLD/USDT:USDT | below_1h_threshold | +2.52% | +2.47% |
| UB/USDT:USDT | below_1h_threshold | +2.44% | +2.40% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
