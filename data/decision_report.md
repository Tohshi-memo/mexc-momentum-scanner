# Decision Report

- generated_at: 2026-05-07T05:32:33.222652+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3572**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3572, expectancy=-0.16%
- 直近20件 MARKET基準: n=20, expectancy=-0.73%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.73% | **-0.73%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618 | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +0.10% | **+0.02%** |
| ASK | 20/20 | 100.0% | -0.10% | **-0.10%** |
| LIMIT_BB3S | 6/15 | 40.0% | -0.26% | **-0.10%** |
| LIMIT_1PCT | 19/20 | 95.0% | -0.13% | **-0.12%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +1.81% | **+1.54%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +1.59% | **+1.11%** |
| LIMIT_BB3S_LONG | 2/4 | 50.0% | +1.54% | **+0.77%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +1.25% | **+0.75%** |
| ASK_LONG | 20/20 | 100.0% | +0.57% | **+0.57%** |

## 2. $100 Live Portfolio

- 残高: **$101.34** / 初期 $100.00 (+1.34%)
- 確定トレード: 19件 (TP 6 / SL 11 / EXP 2)
- 最新: TAG/USDT:USDT TP_HIT PnL +8.00% 残高後 $101.34
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$107.64** / 初期 $100.00 (+7.64%)
- 確定: 66件 (Win 25 / Loss 24 / Flat 17) / skip 67件
- 成長率目線: 平均log +0.001115 / 幾何平均 +0.112% per trade / maxDD +2.48%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SATO/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.63% 残高後 $107.64

## 4. Latest Market Context

- 更新: 2026-05-07T05:32:29.715475+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.18% price=81087.6
- Funnel: target 770 → liquid 186 → pre 50 → checked 50 → surge 3 → strict 0
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 74.5 >= 65=1, 4h RSI 77.0 >= 65=1, 4h RSI 77.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SATO/USDT:USDT | +234.14% | $1,701,340.05 |
| B3/USDT:USDT | +110.73% | $9,177,514.90 |
| DOGS/USDT:USDT | +79.66% | $11,342,936.40 |
| PENGUIN/USDT:USDT | +51.79% | $1,355,193.34 |
| HMSTR/USDT:USDT | +32.52% | $1,080,459.51 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PUMPFUN/USDT:USDT | below_1h_threshold | +4.00% | +3.82% |
| S/USDT:USDT | below_1h_threshold | +3.55% | +3.37% |
| OP/USDT:USDT | below_1h_threshold | +2.98% | +2.80% |
| BLESS/USDT:USDT | below_1h_threshold | +1.88% | +1.70% |
| TONCOIN/USDT:USDT | below_1h_threshold | +1.80% | +1.62% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
