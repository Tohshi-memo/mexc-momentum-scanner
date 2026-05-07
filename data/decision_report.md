# Decision Report

- generated_at: 2026-05-07T04:32:41.009457+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3565**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3565, expectancy=-0.17%
- 直近20件 MARKET基準: n=20, expectancy=-1.37%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.37% | **-1.37%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618 | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +0.13% | **+0.03%** |
| LIMIT_6PCT | 8/20 | 40.0% | -0.29% | **-0.12%** |
| LIMIT_7PCT | 7/20 | 35.0% | -0.34% | **-0.12%** |
| LIMIT_ATR | 16/20 | 80.0% | -0.22% | **-0.17%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +2.57% | **+2.05%** |
| ASK_LONG | 20/20 | 100.0% | +1.72% | **+1.72%** |
| LIMIT_BB3S_LONG | 4/6 | 66.7% | +2.36% | **+1.57%** |
| MARKET_LONG | 20/20 | 100.0% | +1.34% | **+1.34%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +2.02% | **+1.21%** |

## 2. $100 Live Portfolio

- 残高: **$101.34** / 初期 $100.00 (+1.34%)
- 確定トレード: 19件 (TP 6 / SL 11 / EXP 2)
- 最新: TAG/USDT:USDT TP_HIT PnL +8.00% 残高後 $101.34
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$107.23** / 初期 $100.00 (+7.23%)
- 確定: 59件 (Win 22 / Loss 21 / Flat 16) / skip 67件
- 成長率目線: 平均log +0.001182 / 幾何平均 +0.118% per trade / maxDD +2.48%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: NOT/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.63% 残高後 $107.23

## 4. Latest Market Context

- 更新: 2026-05-07T04:32:37.371883+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.15% price=80920.7
- Funnel: target 769 → liquid 187 → pre 50 → checked 50 → surge 3 → strict 0
- Surge前reject: below_1h_threshold=46, below_relative_strength=1, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 79.3 >= 65=1, 4h RSI 83.3 >= 65=1, 4h RSI 85.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SATO/USDT:USDT | +238.47% | $1,580,391.90 |
| B3/USDT:USDT | +116.74% | $8,525,041.87 |
| DOGS/USDT:USDT | +83.92% | $10,649,142.58 |
| PENGUIN/USDT:USDT | +50.70% | $1,276,737.32 |
| FHE/USDT:USDT | +40.05% | $16,424,928.76 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| IO/USDT:USDT | below_relative_strength | +5.11% | +4.96% |
| FHE/USDT:USDT | below_1h_threshold | +4.97% | +4.82% |
| TONCOIN/USDT:USDT | below_1h_threshold | +4.82% | +4.67% |
| KSM/USDT:USDT | below_1h_threshold | +4.16% | +4.00% |
| HMSTR/USDT:USDT | below_1h_threshold | +3.62% | +3.46% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
