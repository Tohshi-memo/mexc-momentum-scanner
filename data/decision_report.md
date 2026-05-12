# Decision Report

- generated_at: 2026-05-12T16:17:29.233345+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4141**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.79% / filled 20/20。**
- 全期間 MARKET基準: n=4141, expectancy=-0.12%
- 直近20件 MARKET基準: n=20, expectancy=+0.79%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.79% | **+0.79%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +1.06% | **+1.06%** |
| MARKET | 20/20 | 100.0% | +0.79% | **+0.79%** |
| LIMIT_5PCT | 7/20 | 35.0% | +0.95% | **+0.33%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.33% | **+0.29%** |
| LIMIT_6PCT | 2/20 | 10.0% | +1.89% | **+0.19%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +1.00% | **+0.75%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +0.53% | **+0.34%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +2.07% | **+0.31%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +1.70% | **+0.25%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +0.57% | **+0.20%** |

## 2. $100 Live Portfolio

- 残高: **$99.19** / 初期 $100.00 (-0.81%)
- 確定トレード: 34件 (TP 9 / SL 22 / EXP 3)
- 最新: DOGS/USDT:USDT TP_HIT PnL +8.00% 残高後 $99.19
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$117.84** / 初期 $100.00 (+17.84%)
- 確定: 277件 (Win 78 / Loss 96 / Flat 103) / skip 425件
- 成長率目線: 平均log +0.000593 / 幾何平均 +0.059% per trade / maxDD +4.21%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: TRUTH/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $117.84

## 4. Latest Market Context

- 更新: 2026-05-12T16:17:26.439051+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.08% price=80234.5
- Funnel: target 763 → liquid 197 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 92.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| VIC/USDT:USDT | +13.62% | $1,604,471.62 |
| LAB/USDT:USDT | +4.95% | $169,956,428.20 |
| XNY/USDT:USDT | +4.06% | $1,320,415.26 |
| RAVE/USDT:USDT | +3.14% | $6,989,184.16 |
| ASTSSTOCK/USDT:USDT | +2.81% | $8,136,083.88 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| LAB/USDT:USDT | below_1h_threshold | +4.94% | +5.02% |
| XNY/USDT:USDT | below_1h_threshold | +4.06% | +4.15% |
| RAVE/USDT:USDT | below_1h_threshold | +3.26% | +3.35% |
| ASTSSTOCK/USDT:USDT | below_1h_threshold | +2.81% | +2.90% |
| IRYS/USDT:USDT | below_1h_threshold | +2.49% | +2.58% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
