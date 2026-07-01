# Decision Report

- generated_at: 2026-07-01T21:36:48.443452+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8019**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.60% / filled 20/20。**
- 全期間 MARKET基準: n=8019, expectancy=-0.03%
- 直近20件 MARKET基準: n=20, expectancy=+2.60%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.60% | **+2.60%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +2.63% | **+2.63%** |
| MARKET | 20/20 | 100.0% | +2.60% | **+2.60%** |
| LIMIT_7PCT | 6/20 | 30.0% | +1.40% | **+0.42%** |
| LIMIT_8PCT | 5/20 | 25.0% | +1.48% | **+0.37%** |
| LIMIT_1PCT | 14/20 | 70.0% | +0.43% | **+0.30%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 5/20 | 25.0% | +2.13% | **+0.53%** |
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +0.63% | **+0.32%** |
| LIMIT_FIB1618_LONG | 5/20 | 25.0% | +0.88% | **+0.22%** |
| MARKET_LONG | 20/20 | 100.0% | +0.20% | **+0.20%** |
| LIMIT_9PCT_LONG | 9/20 | 45.0% | -0.03% | **-0.02%** |

## 2. $100 Live Portfolio

- 残高: **$102.64** / 初期 $100.00 (+2.64%)
- 確定トレード: 47件 (TP 17 / SL 29 / EXP 1)
- 最新: AGLD/USDT:USDT TP_HIT PnL +8.00% 残高後 $102.64
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$275.05** / 初期 $100.00 (+175.05%)
- 確定: 2416件 (Win 740 / Loss 802 / Flat 874) / skip 2164件
- 成長率目線: 平均log +0.000419 / 幾何平均 +0.042% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: TAIKO/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $275.05

## 4. Robust Adaptive DryRun ($100)

- 残高: **$107.21** / 初期 $100.00 (+7.21%)
- 確定: 536件 (Win 135 / Loss 125 / Flat 276) / skip 894件
- 成長率目線: 平均log +0.000130 / 幾何平均 +0.013% per trade / maxDD +3.03%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: TAIKO/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $107.21

## 5. Latest Market Context

- 更新: 2026-07-01T21:36:42.207266+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.98% price=60690.0
- Funnel: target 825 → liquid 157 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=1, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 80.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TLM/USDT:USDT | +62.12% | $3,164,909.86 |
| LIT/USDT:USDT | +21.01% | $7,668,483.96 |
| TAIKO/USDT:USDT | +16.58% | $21,647,508.97 |
| NOM/USDT:USDT | +14.48% | $5,039,418.56 |
| B/USDT:USDT | +12.03% | $1,057,353.24 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BTW/USDT:USDT | below_relative_strength | +5.13% | +4.14% |
| H/USDT:USDT | below_1h_threshold | +4.18% | +3.20% |
| O/USDT:USDT | below_1h_threshold | +3.75% | +2.76% |
| USELESS/USDT:USDT | below_1h_threshold | +2.62% | +1.64% |
| ADA/USDT:USDT | below_1h_threshold | +2.21% | +1.23% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
