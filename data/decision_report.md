# Decision Report

- generated_at: 2026-05-07T11:42:36.276245+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3621**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.77% / filled 20/20。**
- 全期間 MARKET基準: n=3621, expectancy=-0.16%
- 直近20件 MARKET基準: n=20, expectancy=+0.77%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.77% | **+0.77%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 20/20 | 100.0% | +1.27% | **+1.27%** |
| MARKET | 20/20 | 100.0% | +0.77% | **+0.77%** |
| ASK | 20/20 | 100.0% | +0.73% | **+0.73%** |
| LIMIT_2PCT | 17/20 | 85.0% | +0.79% | **+0.67%** |
| LIMIT_4PCT | 11/20 | 55.0% | +0.36% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 19/20 | 95.0% | +2.06% | **+1.96%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +0.92% | **+0.87%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +1.82% | **+0.73%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +1.09% | **+0.71%** |
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +0.92% | **+0.64%** |

## 2. $100 Live Portfolio

- 残高: **$100.83** / 初期 $100.00 (+0.83%)
- 確定トレード: 20件 (TP 6 / SL 12 / EXP 2)
- 最新: SATO/USDT:USDT SL_HIT PnL -4.00% 残高後 $100.83
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$106.83** / 初期 $100.00 (+6.83%)
- 確定: 115件 (Win 37 / Loss 46 / Flat 32) / skip 67件
- 成長率目線: 平均log +0.000575 / 幾何平均 +0.057% per trade / maxDD +2.62%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: JTO/USDT:USDT `LIMIT_7PCT_LONG` EXPIRED account +0.00% 残高後 $106.83

## 4. Latest Market Context

- 更新: 2026-05-07T11:42:32.925441+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.18% price=80951.8
- Funnel: target 771 → liquid 185 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 72.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| B3/USDT:USDT | +101.22% | $11,688,443.58 |
| PENGUIN/USDT:USDT | +91.13% | $3,634,372.28 |
| SATO/USDT:USDT | +89.64% | $2,305,636.75 |
| DOGS/USDT:USDT | +55.63% | $15,915,935.16 |
| NIL/USDT:USDT | +36.70% | $2,791,255.81 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| JTO/USDT:USDT | below_1h_threshold | +4.58% | +4.39% |
| ENA/USDT:USDT | below_1h_threshold | +4.42% | +4.23% |
| XPL/USDT:USDT | below_1h_threshold | +3.45% | +3.27% |
| BASED/USDT:USDT | below_1h_threshold | +1.96% | +1.77% |
| KSM/USDT:USDT | below_1h_threshold | +1.75% | +1.57% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
