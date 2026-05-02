# Decision Report

- generated_at: 2026-05-02T20:22:10.860502+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **2979**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.55% / filled 20/20。**
- 全期間 MARKET基準: n=2979, expectancy=-0.16%
- 直近20件 MARKET基準: n=20, expectancy=+0.55%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.55% | **+0.55%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +0.61% | **+0.61%** |
| MARKET | 20/20 | 100.0% | +0.55% | **+0.55%** |
| LIMIT_BB3S | 5/14 | 35.7% | +1.45% | **+0.52%** |
| LIMIT_5PCT | 6/20 | 30.0% | +0.95% | **+0.29%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +0.71% | **+0.25%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 5/20 | 25.0% | +6.84% | **+1.71%** |
| LIMIT_9PCT_LONG | 6/20 | 30.0% | +3.70% | **+1.11%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +2.86% | **+1.00%** |
| MARKET_LONG | 20/20 | 100.0% | +0.80% | **+0.80%** |
| ASK_LONG | 20/20 | 100.0% | +0.58% | **+0.58%** |

## 2. $100 Live Portfolio

- 残高: **$102.70** / 初期 $100.00 (+2.70%)
- 確定トレード: 9件 (TP 4 / SL 4 / EXP 1)
- 最新: RAVE/USDT:USDT EXPIRED PnL +5.55% 残高後 $102.70
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-02T20:22:06.638880+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.05% price=78400.0
- Funnel: target 755 → liquid 166 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 86.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| XNY/USDT:USDT | +21.75% | $1,402,860.83 |
| NAORIS/USDT:USDT | +10.78% | $3,906,942.36 |
| LUNC/USDT:USDT | +10.66% | $26,516,545.83 |
| BSB/USDT:USDT | +9.92% | $11,002,734.50 |
| CHILLGUY/USDT:USDT | +9.04% | $1,099,231.05 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BEAT/USDT:USDT | below_1h_threshold | +2.77% | +2.83% |
| CHILLGUY/USDT:USDT | below_1h_threshold | +2.49% | +2.54% |
| ACH/USDT:USDT | below_1h_threshold | +2.27% | +2.32% |
| ORCA/USDT:USDT | below_1h_threshold | +1.80% | +1.85% |
| NAORIS/USDT:USDT | below_1h_threshold | +1.66% | +1.72% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
