# Decision Report

- generated_at: 2026-05-02T09:12:03.486642+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **2883**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.80% / filled 20/20。**
- 全期間 MARKET基準: n=2883, expectancy=-0.12%
- 直近20件 MARKET基準: n=20, expectancy=+0.80%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.80% | **+0.80%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 20/20 | 100.0% | +1.01% | **+1.01%** |
| LIMIT_9PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_10PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| MARKET | 20/20 | 100.0% | +0.80% | **+0.80%** |
| LIMIT_8PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +1.31% | **+1.12%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +0.97% | **+0.73%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +0.94% | **+0.56%** |
| ASK_LONG | 20/20 | 100.0% | +0.50% | **+0.50%** |
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +2.00% | **+0.40%** |

## 2. $100 Live Portfolio

- 残高: **$102.51** / 初期 $100.00 (+2.51%)
- 確定トレード: 7件 (TP 4 / SL 3 / EXP 0)
- 最新: BIO/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.51
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-02T09:12:01.493473+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.02% price=78256.8
- Funnel: target 755 → liquid 165 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 92.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LAB/USDT:USDT | +165.80% | $93,401,851.37 |
| KNC/USDT:USDT | +22.45% | $1,641,481.54 |
| BIO/USDT:USDT | +21.05% | $1,445,836.30 |
| TAC/USDT:USDT | +17.61% | $1,057,756.08 |
| IRYS/USDT:USDT | +16.57% | $1,385,533.10 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| UB/USDT:USDT | below_1h_threshold | +3.29% | +3.31% |
| NAORIS/USDT:USDT | below_1h_threshold | +1.89% | +1.91% |
| BIO/USDT:USDT | below_1h_threshold | +1.83% | +1.85% |
| MOVR/USDT:USDT | below_1h_threshold | +1.35% | +1.37% |
| INJ/USDT:USDT | below_1h_threshold | +1.27% | +1.29% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
