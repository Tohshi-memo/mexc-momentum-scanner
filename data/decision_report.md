# Decision Report

- generated_at: 2026-05-04T07:27:10.907137+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3168**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.07% / filled 20/20。**
- 全期間 MARKET基準: n=3168, expectancy=-0.16%
- 直近20件 MARKET基準: n=20, expectancy=+2.07%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.07% | **+2.07%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.07% | **+2.07%** |
| ASK | 20/20 | 100.0% | +1.92% | **+1.92%** |
| LIMIT_1PCT | 17/20 | 85.0% | +1.51% | **+1.28%** |
| LIMIT_ATR | 12/20 | 60.0% | +1.86% | **+1.12%** |
| LIMIT_2PCT | 13/20 | 65.0% | +1.67% | **+1.09%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +3.40% | **+0.51%** |
| LIMIT_8PCT_LONG | 9/20 | 45.0% | +0.89% | **+0.40%** |
| LIMIT_FIB1272_LONG | 11/20 | 55.0% | +0.04% | **+0.02%** |
| LIMIT_7PCT_LONG | 10/20 | 50.0% | -0.15% | **-0.08%** |
| LIMIT_3PCT_LONG | 15/20 | 75.0% | -0.20% | **-0.15%** |

## 2. $100 Live Portfolio

- 残高: **$103.40** / 初期 $100.00 (+3.40%)
- 確定トレード: 12件 (TP 5 / SL 5 / EXP 2)
- 最新: B2/USDT:USDT EXPIRED PnL +1.44% 残高後 $103.40
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-04T07:27:08.826022+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.00% price=79823.4
- Funnel: target 761 → liquid 176 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 86.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SKYAI/USDT:USDT | +56.31% | $48,507,509.51 |
| BSB/USDT:USDT | +54.33% | $24,554,520.70 |
| LAB/USDT:USDT | +36.68% | $214,936,941.84 |
| TST/USDT:USDT | +36.36% | $6,743,106.89 |
| TAG/USDT:USDT | +35.44% | $11,213,768.95 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SKYAI/USDT:USDT | below_1h_threshold | +3.46% | +3.46% |
| SIREN/USDT:USDT | below_1h_threshold | +2.87% | +2.87% |
| BSB/USDT:USDT | below_1h_threshold | +2.77% | +2.77% |
| LUNC/USDT:USDT | below_1h_threshold | +2.69% | +2.69% |
| GIGGLE/USDT:USDT | below_1h_threshold | +2.19% | +2.19% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
