# Decision Report

- generated_at: 2026-05-01T20:16:57.122267+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **2829**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.23% / filled 20/20。**
- 全期間 MARKET基準: n=2829, expectancy=-0.12%
- 直近20件 MARKET基準: n=20, expectancy=+1.23%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.23% | **+1.23%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +1.47% | **+1.47%** |
| MARKET | 20/20 | 100.0% | +1.23% | **+1.23%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.93% | **+0.84%** |
| LIMIT_2PCT | 15/20 | 75.0% | +0.32% | **+0.24%** |
| LIMIT_5PCT | 4/20 | 20.0% | +0.95% | **+0.19%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/8 | 37.5% | +2.96% | **+1.11%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +2.00% | **+0.80%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +0.68% | **+0.51%** |
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +0.71% | **+0.50%** |
| LIMIT_ATR_LONG | 15/20 | 75.0% | +0.52% | **+0.39%** |

## 2. $100 Live Portfolio

- 残高: **$103.54** / 初期 $100.00 (+3.54%)
- 確定トレード: 5件 (TP 4 / SL 1 / EXP 0)
- 最新: NAORIS/USDT:USDT TP_HIT PnL +8.00% 残高後 $103.54
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-01T20:16:55.153394+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.10% price=78239.3
- Funnel: target 756 → liquid 189 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 71.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LAB/USDT:USDT | +23.95% | $2,798,485.81 |
| TAG/USDT:USDT | +12.00% | $3,164,944.63 |
| ZEN/USDT:USDT | +10.77% | $6,514,331.94 |
| FIGHT/USDT:USDT | +8.18% | $1,226,713.58 |
| SQD/USDT:USDT | +7.75% | $2,097,187.52 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TAG/USDT:USDT | below_1h_threshold | +2.17% | +2.27% |
| ZEN/USDT:USDT | below_1h_threshold | +1.78% | +1.88% |
| CHIP/USDT:USDT | below_1h_threshold | +1.27% | +1.37% |
| BIO/USDT:USDT | below_1h_threshold | +1.18% | +1.28% |
| CRCLSTOCK/USDT:USDT | below_1h_threshold | +0.92% | +1.02% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
