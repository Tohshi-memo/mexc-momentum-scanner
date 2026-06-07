# Decision Report

- generated_at: 2026-06-07T22:21:38.490039+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6003**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.27% / filled 20/20。**
- 全期間 MARKET基準: n=6003, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=+0.27%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.27% | **+0.27%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 4/16 | 25.0% | +1.84% | **+0.46%** |
| ASK | 20/20 | 100.0% | +0.35% | **+0.35%** |
| MARKET | 20/20 | 100.0% | +0.27% | **+0.27%** |
| LIMIT_5PCT | 5/20 | 25.0% | +0.95% | **+0.24%** |
| LIMIT_6PCT | 2/20 | 10.0% | +1.89% | **+0.19%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 4/4 | 100.0% | +3.16% | **+3.16%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +8.00% | **+1.20%** |
| LIMIT_3PCT_LONG | 15/20 | 75.0% | +1.48% | **+1.11%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +1.27% | **+1.02%** |
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +1.00% | **+0.45%** |

## 2. $100 Live Portfolio

- 残高: **$99.00** / 初期 $100.00 (-1.00%)
- 確定トレード: 5件 (TP 1 / SL 4 / EXP 0)
- 最新: BSB/USDT:USDT SL_HIT PnL -4.00% 残高後 $99.00
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$155.01** / 初期 $100.00 (+55.01%)
- 確定: 1120件 (Win 274 / Loss 337 / Flat 509) / skip 1444件
- 成長率目線: 平均log +0.000391 / 幾何平均 +0.039% per trade / maxDD +7.25%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BEAT/USDT:USDT `LIMIT_2PCT_LONG` TP_HIT account +1.00% 残高後 $155.01

## 4. Latest Market Context

- 更新: 2026-06-07T22:21:35.629643+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +2.31% price=63180.8
- Funnel: target 768 → liquid 130 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=46, below_relative_strength=3, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 88.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BANK/USDT:USDT | +27.73% | $3,940,069.35 |
| BEAT/USDT:USDT | +27.51% | $74,200,515.14 |
| BTW/USDT:USDT | +27.15% | $13,752,543.29 |
| PIPPIN/USDT:USDT | +17.50% | $3,749,870.34 |
| BLESS/USDT:USDT | +15.73% | $8,181,017.71 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BLESS/USDT:USDT | below_relative_strength | +7.08% | +4.77% |
| MYX/USDT:USDT | below_relative_strength | +5.95% | +3.65% |
| PIPPIN/USDT:USDT | below_relative_strength | +5.24% | +2.93% |
| OP/USDT:USDT | below_1h_threshold | +4.79% | +2.48% |
| SIREN/USDT:USDT | below_1h_threshold | +4.53% | +2.22% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
