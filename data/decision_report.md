# Decision Report

- generated_at: 2026-05-28T06:58:33.569755+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4955**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.49% / filled 20/20。**
- 全期間 MARKET基準: n=4955, expectancy=-0.07%
- 直近20件 MARKET基準: n=20, expectancy=+1.49%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.49% | **+1.49%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT | 16/20 | 80.0% | +3.42% | **+2.73%** |
| LIMIT_3PCT | 13/20 | 65.0% | +3.54% | **+2.30%** |
| LIMIT_1PCT | 17/20 | 85.0% | +2.33% | **+1.98%** |
| MARKET | 20/20 | 100.0% | +1.49% | **+1.49%** |
| ASK | 20/20 | 100.0% | +0.88% | **+0.88%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +3.03% | **+1.21%** |
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +5.17% | **+1.03%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +3.91% | **+0.98%** |
| LIMIT_7PCT_LONG | 10/20 | 50.0% | +0.76% | **+0.38%** |
| LIMIT_BB3S_LONG | 3/7 | 42.9% | +0.46% | **+0.20%** |

## 2. $100 Live Portfolio

- 残高: **$98.12** / 初期 $100.00 (-1.88%)
- 確定トレード: 69件 (TP 20 / SL 46 / EXP 3)
- 最新: ASTEROID/USDT:USDT TP_HIT PnL +8.00% 残高後 $98.12
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$126.79** / 初期 $100.00 (+26.79%)
- 確定: 690件 (Win 172 / Loss 220 / Flat 298) / skip 826件
- 成長率目線: 平均log +0.000344 / 幾何平均 +0.034% per trade / maxDD +4.72%
- 次の候補: `LIMIT_8PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SKYAI/USDT:USDT `LIMIT_8PCT_LONG` EXPIRED account +0.00% 残高後 $126.79

## 4. Latest Market Context

- 更新: 2026-05-28T06:58:29.546701+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.22% price=73116.9
- Funnel: target 777 → liquid 157 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SNOWSTOCK/USDT:USDT | +34.92% | $7,884,959.06 |
| NBISSTOCK/USDT:USDT | +12.80% | $1,715,241.92 |
| BILL/USDT:USDT | +9.82% | $10,870,379.45 |
| GENIUS/USDT:USDT | +6.37% | $2,597,695.25 |
| XLM/USDT:USDT | +5.51% | $99,434,675.84 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ESPORTS/USDT:USDT | below_1h_threshold | +2.23% | +2.01% |
| NIGHT/USDT:USDT | below_1h_threshold | +2.02% | +1.81% |
| BUILDONBOB/USDT:USDT | below_1h_threshold | +1.44% | +1.22% |
| WLFI/USDT:USDT | below_1h_threshold | +1.21% | +1.00% |
| XLM/USDT:USDT | below_1h_threshold | +1.02% | +0.80% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
