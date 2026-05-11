# Decision Report

- generated_at: 2026-05-11T08:57:58.395969+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4021**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.65% / filled 20/20。**
- 全期間 MARKET基準: n=4021, expectancy=-0.12%
- 直近20件 MARKET基準: n=20, expectancy=+0.65%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.65% | **+0.65%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT | 14/20 | 70.0% | +1.07% | **+0.75%** |
| MARKET | 20/20 | 100.0% | +0.65% | **+0.65%** |
| LIMIT_5PCT | 4/20 | 20.0% | +2.71% | **+0.54%** |
| LIMIT_6PCT | 2/20 | 10.0% | +4.94% | **+0.49%** |
| LIMIT_4PCT | 10/20 | 50.0% | +0.83% | **+0.42%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 10/11 | 90.9% | +0.17% | **+0.16%** |
| LIMIT_FIB1272_LONG | 12/20 | 60.0% | +0.24% | **+0.15%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | -0.48% | **-0.05%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | -0.10% | **-0.07%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | -0.21% | **-0.12%** |

## 2. $100 Live Portfolio

- 残高: **$98.21** / 初期 $100.00 (-1.79%)
- 確定トレード: 33件 (TP 8 / SL 22 / EXP 3)
- 最新: SIREN/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.21
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$107.86** / 初期 $100.00 (+7.86%)
- 確定: 218件 (Win 54 / Loss 76 / Flat 88) / skip 364件
- 成長率目線: 平均log +0.000347 / 幾何平均 +0.035% per trade / maxDD +4.09%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: B/USDT:USDT `LIMIT_ATR_LONG` SL_HIT account -0.50% 残高後 $107.86

## 4. Latest Market Context

- 更新: 2026-05-11T08:57:51.599823+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.05% price=80749.1
- Funnel: target 760 → liquid 178 → pre 50 → checked 50 → surge 2 → strict 2
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| US/USDT:USDT | +37.39% | $11,859,391.25 |
| B/USDT:USDT | +25.38% | $8,210,512.17 |
| VVV/USDT:USDT | +19.21% | $14,192,183.99 |
| ALCH/USDT:USDT | +17.81% | $4,637,739.98 |
| SAGA/USDT:USDT | +17.72% | $1,994,835.49 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| UB/USDT:USDT | below_1h_threshold | +4.59% | +4.54% |
| H/USDT:USDT | below_1h_threshold | +2.72% | +2.67% |
| CRCLSTOCK/USDT:USDT | below_1h_threshold | +2.34% | +2.29% |
| KITE/USDT:USDT | below_1h_threshold | +2.32% | +2.27% |
| TRUTH/USDT:USDT | below_1h_threshold | +2.14% | +2.09% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
