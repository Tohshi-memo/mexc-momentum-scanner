# Decision Report

- generated_at: 2026-06-07T06:21:30.898105+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5928**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=5928, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=-0.26%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.26% | **-0.26%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 5/20 | 25.0% | +2.80% | **+0.70%** |
| LIMIT_BB3S | 7/15 | 46.7% | +1.21% | **+0.57%** |
| LIMIT_8PCT | 3/20 | 15.0% | +3.70% | **+0.56%** |
| LIMIT_5PCT | 9/20 | 45.0% | +0.40% | **+0.18%** |
| LIMIT_6PCT | 5/20 | 25.0% | +0.71% | **+0.18%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +3.25% | **+1.30%** |
| MARKET_LONG | 20/20 | 100.0% | +0.66% | **+0.66%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +4.15% | **+0.62%** |
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +1.10% | **+0.38%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +1.55% | **+0.31%** |

## 2. $100 Live Portfolio

- 残高: **$99.99** / 初期 $100.00 (-0.01%)
- 確定トレード: 3件 (TP 1 / SL 2 / EXP 0)
- 最新: LAB/USDT:USDT TP_HIT PnL +8.00% 残高後 $99.99
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$138.77** / 初期 $100.00 (+38.77%)
- 確定: 1047件 (Win 252 / Loss 321 / Flat 474) / skip 1442件
- 成長率目線: 平均log +0.000313 / 幾何平均 +0.031% per trade / maxDD +7.25%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BSB/USDT:USDT `LIMIT_1PCT_LONG` TP_HIT account +1.00% 残高後 $138.77

## 4. Latest Market Context

- 更新: 2026-06-07T06:21:28.288019+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.05% price=61743.0
- Funnel: target 771 → liquid 126 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| FIDA/USDT:USDT | +57.85% | $5,217,220.70 |
| LAB/USDT:USDT | +38.97% | $64,136,868.76 |
| BSB/USDT:USDT | +25.42% | $4,747,369.51 |
| BLESS/USDT:USDT | +21.91% | $4,538,759.49 |
| EDEN/USDT:USDT | +21.38% | $1,631,856.72 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| HOME/USDT:USDT | below_1h_threshold | +3.39% | +3.34% |
| BSB/USDT:USDT | below_1h_threshold | +3.28% | +3.23% |
| H/USDT:USDT | below_1h_threshold | +2.00% | +1.94% |
| CLO/USDT:USDT | below_1h_threshold | +1.50% | +1.45% |
| JTO/USDT:USDT | below_1h_threshold | +1.32% | +1.27% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
