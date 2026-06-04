# Decision Report

- generated_at: 2026-06-04T03:18:55.855137+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5597**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +3.82% / filled 20/20。**
- 全期間 MARKET基準: n=5597, expectancy=-0.03%
- 直近20件 MARKET基準: n=20, expectancy=+3.82%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +3.82% | **+3.82%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +4.00% | **+4.00%** |
| MARKET | 20/20 | 100.0% | +3.82% | **+3.82%** |
| LIMIT_1PCT | 16/20 | 80.0% | +3.29% | **+2.64%** |
| LIMIT_2PCT | 12/20 | 60.0% | +3.04% | **+1.82%** |
| LIMIT_ATR | 10/20 | 50.0% | +3.55% | **+1.78%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 7/20 | 35.0% | +2.34% | **+0.82%** |
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +3.67% | **+0.73%** |
| LIMIT_8PCT_LONG | 11/20 | 55.0% | +0.00% | **+0.00%** |
| LIMIT_FIB1618_LONG | 7/20 | 35.0% | -0.63% | **-0.22%** |
| LIMIT_7PCT_LONG | 12/20 | 60.0% | -0.90% | **-0.54%** |

## 2. $100 Live Portfolio

- 残高: **$99.04** / 初期 $100.00 (-0.96%)
- 確定トレード: 94件 (TP 29 / SL 62 / EXP 3)
- 最新: ICP/USDT:USDT TP_HIT PnL +8.00% 残高後 $99.04
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$131.20** / 初期 $100.00 (+31.20%)
- 確定: 1005件 (Win 239 / Loss 312 / Flat 454) / skip 1153件
- 成長率目線: 平均log +0.000270 / 幾何平均 +0.027% per trade / maxDD +7.25%
- 次の候補: `LIMIT_10PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: LIT/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $131.20

## 4. Latest Market Context

- 更新: 2026-06-04T03:18:53.738024+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +1.32% price=64032.6
- Funnel: target 771 → liquid 154 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=47, below_relative_strength=2, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 76.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| OPN/USDT:USDT | +31.48% | $23,941,696.74 |
| EPIC/USDT:USDT | +20.11% | $3,689,342.47 |
| STO/USDT:USDT | +17.41% | $6,998,020.50 |
| BP/USDT:USDT | +11.60% | $1,578,748.75 |
| MAGMA/USDT:USDT | +10.25% | $4,519,498.60 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| OPN/USDT:USDT | below_relative_strength | +6.03% | +4.71% |
| ONDO/USDT:USDT | below_relative_strength | +5.15% | +3.83% |
| US/USDT:USDT | below_1h_threshold | +4.84% | +3.52% |
| AIA/USDT:USDT | below_1h_threshold | +4.74% | +3.42% |
| DYDX/USDT:USDT | below_1h_threshold | +4.25% | +2.93% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
