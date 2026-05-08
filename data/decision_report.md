# Decision Report

- generated_at: 2026-05-08T01:12:35.558516+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3718**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.13% / filled 20/20。**
- 全期間 MARKET基準: n=3718, expectancy=-0.16%
- 直近20件 MARKET基準: n=20, expectancy=+1.13%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.13% | **+1.13%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.13% | **+1.13%** |
| ASK | 20/20 | 100.0% | +1.03% | **+1.03%** |
| LIMIT_9PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_8PCT | 4/20 | 20.0% | +2.85% | **+0.57%** |
| LIMIT_ATR | 7/20 | 35.0% | +1.59% | **+0.56%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +0.41% | **+0.41%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +1.00% | **+0.40%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +2.07% | **+0.31%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | +1.47% | **+0.22%** |
| LIMIT_ATR_LONG | 9/20 | 45.0% | +0.30% | **+0.14%** |

## 2. $100 Live Portfolio

- 残高: **$99.32** / 初期 $100.00 (-0.68%)
- 確定トレード: 23件 (TP 6 / SL 15 / EXP 2)
- 最新: D/USDT:USDT SL_HIT PnL -4.00% 残高後 $99.32
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$108.41** / 初期 $100.00 (+8.41%)
- 確定: 189件 (Win 48 / Loss 64 / Flat 77) / skip 90件
- 成長率目線: 平均log +0.000427 / 幾何平均 +0.043% per trade / maxDD +3.48%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: FHE/USDT:USDT `LIMIT_4PCT_LONG` SL_HIT account -0.50% 残高後 $108.41

## 4. Latest Market Context

- 更新: 2026-05-08T01:12:32.127858+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.08% price=79730.4
- Funnel: target 767 → liquid 185 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SATO/USDT:USDT | +21.74% | $8,615,690.61 |
| LAB/USDT:USDT | +18.82% | $211,897,485.89 |
| TST/USDT:USDT | +17.80% | $6,150,702.80 |
| NOT/USDT:USDT | +16.86% | $10,933,537.97 |
| DYDX/USDT:USDT | +16.13% | $10,629,951.15 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| B3/USDT:USDT | below_1h_threshold | +2.53% | +2.62% |
| BSB/USDT:USDT | below_1h_threshold | +1.50% | +1.58% |
| B/USDT:USDT | below_1h_threshold | +1.38% | +1.46% |
| CHIP/USDT:USDT | below_1h_threshold | +0.83% | +0.91% |
| BASED/USDT:USDT | below_1h_threshold | +0.68% | +0.76% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
