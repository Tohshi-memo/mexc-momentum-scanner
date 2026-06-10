# Decision Report

- generated_at: 2026-06-10T20:49:11.771887+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6263**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6263, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=-0.41%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.41% | **-0.41%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| ASK | 20/20 | 100.0% | +0.44% | **+0.44%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_5PCT | 10/20 | 50.0% | +0.17% | **+0.09%** |
| LIMIT_9PCT | 3/20 | 15.0% | -0.00% | **-0.00%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.01% | **+1.01%** |
| ASK_LONG | 20/20 | 100.0% | +0.83% | **+0.83%** |
| LIMIT_1PCT_LONG | 14/20 | 70.0% | +0.73% | **+0.51%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +1.70% | **+0.25%** |
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +0.72% | **+0.21%** |

## 2. $100 Live Portfolio

- 残高: **$95.18** / 初期 $100.00 (-4.82%)
- 確定トレード: 14件 (TP 1 / SL 12 / EXP 1)
- 最新: H/USDT:USDT SL_HIT PnL -4.00% 残高後 $95.18
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$151.23** / 初期 $100.00 (+51.23%)
- 確定: 1249件 (Win 312 / Loss 388 / Flat 549) / skip 1575件
- 成長率目線: 平均log +0.000331 / 幾何平均 +0.033% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: VELVET/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $151.23

## 4. Latest Market Context

- 更新: 2026-06-10T20:49:04.118356+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.24% price=61762.6
- Funnel: target 785 → liquid 154 → pre 50 → checked 50 → surge 4 → strict 2
- Surge前reject: below_1h_threshold=46, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 82.4 >= 65=1, 4h RSI 87.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| VELVET/USDT:USDT | +74.31% | $27,734,797.72 |
| BEAT/USDT:USDT | +28.83% | $146,125,424.11 |
| JCT/USDT:USDT | +14.52% | $2,290,377.29 |
| SKYAI/USDT:USDT | +9.16% | $5,524,990.26 |
| STRAX/USDT:USDT | +6.34% | $1,215,788.03 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| H/USDT:USDT | below_1h_threshold | +4.85% | +5.09% |
| JCT/USDT:USDT | below_1h_threshold | +4.53% | +4.77% |
| STRAX/USDT:USDT | below_1h_threshold | +3.68% | +3.91% |
| HMSTR/USDT:USDT | below_1h_threshold | +3.35% | +3.59% |
| AGT/USDT:USDT | below_1h_threshold | +2.63% | +2.87% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
