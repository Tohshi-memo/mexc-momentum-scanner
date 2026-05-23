# Decision Report

- generated_at: 2026-05-23T10:29:00.590195+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4768**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.11% / filled 20/20。**
- 全期間 MARKET基準: n=4768, expectancy=-0.08%
- 直近20件 MARKET基準: n=20, expectancy=+2.11%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.11% | **+2.11%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.11% | **+2.11%** |
| ASK | 20/20 | 100.0% | +2.05% | **+2.05%** |
| LIMIT_1PCT | 16/20 | 80.0% | +0.95% | **+0.76%** |
| LIMIT_ATR | 11/20 | 55.0% | +0.68% | **+0.37%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +0.79% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +4.15% | **+0.62%** |
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +0.33% | **+0.28%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +1.10% | **+0.22%** |
| MARKET_LONG | 20/20 | 100.0% | +0.06% | **+0.06%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +0.03% | **+0.02%** |

## 2. $100 Live Portfolio

- 残高: **$97.16** / 初期 $100.00 (-2.84%)
- 確定トレード: 62件 (TP 17 / SL 42 / EXP 3)
- 最新: DASH/USDT:USDT TP_HIT PnL +6.60% 残高後 $97.16
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$121.52** / 初期 $100.00 (+21.52%)
- 確定: 614件 (Win 150 / Loss 194 / Flat 270) / skip 715件
- 成長率目線: 平均log +0.000317 / 幾何平均 +0.032% per trade / maxDD +4.21%
- 次の候補: `LIMIT_7PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BSB/USDT:USDT `LIMIT_7PCT_LONG` EXPIRED account +0.00% 残高後 $121.52

## 4. Latest Market Context

- 更新: 2026-05-23T10:28:57.978926+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.09% price=74696.2
- Funnel: target 764 → liquid 132 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 80.2 >= 65=1, 4h RSI 65.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BSB/USDT:USDT | +170.15% | $73,738,183.99 |
| BEAT/USDT:USDT | +25.84% | $66,502,256.15 |
| GMTTOKEN/USDT:USDT | +19.52% | $2,632,195.99 |
| IN/USDT:USDT | +16.12% | $1,988,597.04 |
| TAG/USDT:USDT | +12.85% | $1,453,009.58 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BILL/USDT:USDT | below_1h_threshold | +4.92% | +4.83% |
| MYX/USDT:USDT | below_1h_threshold | +3.48% | +3.39% |
| IN/USDT:USDT | below_1h_threshold | +2.74% | +2.65% |
| H/USDT:USDT | below_1h_threshold | +2.33% | +2.24% |
| TAG/USDT:USDT | below_1h_threshold | +1.57% | +1.48% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
