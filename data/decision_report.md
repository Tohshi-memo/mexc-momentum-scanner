# Decision Report

- generated_at: 2026-05-05T00:37:22.815174+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3281**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.10% / filled 20/20。**
- 全期間 MARKET基準: n=3281, expectancy=-0.16%
- 直近20件 MARKET基準: n=20, expectancy=+1.10%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.10% | **+1.10%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.10% | **+1.10%** |
| ASK | 20/20 | 100.0% | +1.04% | **+1.04%** |
| LIMIT_1PCT | 16/20 | 80.0% | +1.03% | **+0.83%** |
| LIMIT_BB3S | 3/11 | 27.3% | +2.22% | **+0.60%** |
| LIMIT_9PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +6.27% | **+1.25%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +8.00% | **+1.20%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +1.36% | **+0.54%** |
| LIMIT_FIB1272_LONG | 13/20 | 65.0% | +0.66% | **+0.43%** |
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +1.33% | **+0.40%** |

## 2. $100 Live Portfolio

- 残高: **$101.85** / 初期 $100.00 (+1.85%)
- 確定トレード: 15件 (TP 5 / SL 8 / EXP 2)
- 最新: RAVE/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.85
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-05T00:37:20.449351+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.24% price=80016.2
- Funnel: target 761 → liquid 203 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 68.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| RAVE/USDT:USDT | +32.41% | $58,291,987.13 |
| FHE/USDT:USDT | +21.23% | $2,655,198.54 |
| TONCOIN/USDT:USDT | +15.52% | $42,289,328.32 |
| PLAY/USDT:USDT | +11.68% | $2,650,586.13 |
| LAB/USDT:USDT | +10.59% | $103,579,951.56 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| RAVE/USDT:USDT | below_1h_threshold | +4.18% | +3.94% |
| ENSO/USDT:USDT | below_1h_threshold | +3.51% | +3.27% |
| TST/USDT:USDT | below_1h_threshold | +2.81% | +2.57% |
| OL/USDT:USDT | below_1h_threshold | +1.69% | +1.45% |
| H/USDT:USDT | below_1h_threshold | +1.52% | +1.28% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
