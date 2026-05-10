# Decision Report

- generated_at: 2026-05-10T01:47:38.788648+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3933**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.50% / filled 20/20。**
- 全期間 MARKET基準: n=3933, expectancy=-0.12%
- 直近20件 MARKET基準: n=20, expectancy=+0.50%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.50% | **+0.50%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +1.21% | **+1.21%** |
| LIMIT_1PCT | 17/20 | 85.0% | +0.67% | **+0.57%** |
| MARKET | 20/20 | 100.0% | +0.50% | **+0.50%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |
| LIMIT_2PCT | 15/20 | 75.0% | +0.29% | **+0.22%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT_LONG | 11/20 | 55.0% | +1.77% | **+0.97%** |
| LIMIT_6PCT_LONG | 8/20 | 40.0% | +2.41% | **+0.96%** |
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +1.27% | **+0.44%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +1.10% | **+0.11%** |
| LIMIT_1PCT_LONG | 20/20 | 100.0% | +0.04% | **+0.04%** |

## 2. $100 Live Portfolio

- 残高: **$98.21** / 初期 $100.00 (-1.79%)
- 確定トレード: 30件 (TP 7 / SL 20 / EXP 3)
- 最新: SATO/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.21
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$107.73** / 初期 $100.00 (+7.73%)
- 確定: 196件 (Win 48 / Loss 66 / Flat 82) / skip 298件
- 成長率目線: 平均log +0.000380 / 幾何平均 +0.038% per trade / maxDD +4.09%
- 次の候補: `LIMIT_5PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: LAB/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $107.73

## 4. Latest Market Context

- 更新: 2026-05-10T01:47:35.663818+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.04% price=80599.7
- Funnel: target 769 → liquid 171 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 69.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| INX/USDT:USDT | +35.54% | $12,801,358.13 |
| SATO/USDT:USDT | +30.85% | $5,787,712.69 |
| BILL/USDT:USDT | +14.08% | $39,344,960.70 |
| BRETT/USDT:USDT | +11.56% | $2,533,115.90 |
| JASMY/USDT:USDT | +10.12% | $16,992,264.64 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BRETT/USDT:USDT | below_1h_threshold | +2.38% | +2.42% |
| XNY/USDT:USDT | below_1h_threshold | +1.06% | +1.10% |
| TONCOIN/USDT:USDT | below_1h_threshold | +1.01% | +1.06% |
| COLLECT/USDT:USDT | below_1h_threshold | +0.79% | +0.83% |
| BILL/USDT:USDT | below_1h_threshold | +0.51% | +0.55% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
