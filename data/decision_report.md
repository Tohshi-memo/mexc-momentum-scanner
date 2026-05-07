# Decision Report

- generated_at: 2026-05-07T20:53:03.863844+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3696**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.26% / filled 20/20。**
- 全期間 MARKET基準: n=3696, expectancy=-0.16%
- 直近20件 MARKET基準: n=20, expectancy=+0.26%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.26% | **+0.26%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 2/16 | 12.5% | +3.66% | **+0.46%** |
| LIMIT_1PCT | 19/20 | 95.0% | +0.29% | **+0.28%** |
| MARKET | 20/20 | 100.0% | +0.26% | **+0.26%** |
| LIMIT_5PCT | 5/20 | 25.0% | +0.95% | **+0.24%** |
| LIMIT_6PCT | 2/20 | 10.0% | +1.89% | **+0.19%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/4 | 75.0% | +2.21% | **+1.66%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +1.32% | **+0.79%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +0.93% | **+0.56%** |
| LIMIT_9PCT_LONG | 7/20 | 35.0% | +1.10% | **+0.38%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +0.44% | **+0.35%** |

## 2. $100 Live Portfolio

- 残高: **$99.82** / 初期 $100.00 (-0.18%)
- 確定トレード: 22件 (TP 6 / SL 14 / EXP 2)
- 最新: LAB/USDT:USDT SL_HIT PnL -4.00% 残高後 $99.82
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$108.41** / 初期 $100.00 (+8.41%)
- 確定: 189件 (Win 48 / Loss 64 / Flat 77) / skip 68件
- 成長率目線: 平均log +0.000427 / 幾何平均 +0.043% per trade / maxDD +3.48%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: FHE/USDT:USDT `LIMIT_4PCT_LONG` SL_HIT account -0.50% 残高後 $108.41

## 4. Latest Market Context

- 更新: 2026-05-07T20:52:57.156704+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.19% price=79934.6
- Funnel: target 766 → liquid 189 → pre 50 → checked 50 → surge 5 → strict 2
- Surge前reject: below_1h_threshold=45, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 79.9 >= 65=1, 4h RSI 78.0 >= 65=1, 4h RSI 96.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TST/USDT:USDT | +37.92% | $5,148,696.59 |
| SATO/USDT:USDT | +34.01% | $6,358,990.01 |
| NIL/USDT:USDT | +27.44% | $11,964,729.14 |
| NOT/USDT:USDT | +18.85% | $9,688,914.77 |
| JTO/USDT:USDT | +16.22% | $16,248,424.67 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| NOT/USDT:USDT | below_1h_threshold | +2.34% | +2.54% |
| LINEA/USDT:USDT | below_1h_threshold | +2.10% | +2.29% |
| HMSTR/USDT:USDT | below_1h_threshold | +1.83% | +2.02% |
| LIGHT/USDT:USDT | below_1h_threshold | +1.59% | +1.79% |
| USOIL/USDT:USDT | below_1h_threshold | +0.76% | +0.96% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
