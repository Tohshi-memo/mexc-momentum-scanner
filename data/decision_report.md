# Decision Report

- generated_at: 2026-05-25T19:19:24.199909+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4869**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.21% / filled 20/20。**
- 全期間 MARKET基準: n=4869, expectancy=-0.09%
- 直近20件 MARKET基準: n=20, expectancy=+0.21%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.21% | **+0.21%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +0.77% | **+0.77%** |
| LIMIT_6PCT | 5/20 | 25.0% | +0.85% | **+0.21%** |
| MARKET | 20/20 | 100.0% | +0.21% | **+0.21%** |
| LIMIT_5PCT | 8/20 | 40.0% | +0.43% | **+0.17%** |
| LIMIT_7PCT | 3/20 | 15.0% | +0.76% | **+0.11%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 15/20 | 75.0% | +1.48% | **+1.11%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +1.21% | **+0.91%** |
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +1.89% | **+0.85%** |
| LIMIT_ATR_LONG | 15/20 | 75.0% | +0.74% | **+0.56%** |
| LIMIT_5PCT_LONG | 11/20 | 55.0% | +0.77% | **+0.42%** |

## 2. $100 Live Portfolio

- 残高: **$96.68** / 初期 $100.00 (-3.32%)
- 確定トレード: 63件 (TP 17 / SL 43 / EXP 3)
- 最新: KITE/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.68
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$127.31** / 初期 $100.00 (+27.31%)
- 確定: 673件 (Win 169 / Loss 214 / Flat 290) / skip 757件
- 成長率目線: 平均log +0.000359 / 幾何平均 +0.036% per trade / maxDD +4.72%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: IN/USDT:USDT `LIMIT_ATR_LONG` SL_HIT account -0.50% 残高後 $127.31

## 4. Latest Market Context

- 更新: 2026-05-25T19:19:19.478202+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.13% price=77413.5
- Funnel: target 765 → liquid 124 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| POND/USDT:USDT | +72.85% | $1,360,681.62 |
| PHA/USDT:USDT | +10.69% | $4,453,045.12 |
| WLD/USDT:USDT | +8.66% | $32,211,327.32 |
| NIL/USDT:USDT | +7.90% | $16,873,824.21 |
| GRASS/USDT:USDT | +6.64% | $4,257,353.31 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PHA/USDT:USDT | below_1h_threshold | +4.32% | +4.44% |
| POND/USDT:USDT | below_1h_threshold | +4.29% | +4.42% |
| AKT/USDT:USDT | below_1h_threshold | +3.66% | +3.79% |
| LIT/USDT:USDT | below_1h_threshold | +1.48% | +1.60% |
| WLD/USDT:USDT | below_1h_threshold | +1.41% | +1.54% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
