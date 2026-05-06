# Decision Report

- generated_at: 2026-05-06T08:42:37.046369+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3435**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3435, expectancy=-0.14%
- 直近20件 MARKET基準: n=20, expectancy=-0.22%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.22% | **-0.22%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 2/20 | 10.0% | +6.29% | **+0.63%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.80% | **+0.42%** |
| LIMIT_6PCT | 4/20 | 20.0% | +1.89% | **+0.38%** |
| LIMIT_8PCT | 2/20 | 10.0% | +3.70% | **+0.37%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | +0.35% | **+0.14%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +1.82% | **+1.64%** |
| MARKET_LONG | 20/20 | 100.0% | +0.97% | **+0.97%** |
| ASK_LONG | 20/20 | 100.0% | +0.90% | **+0.90%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +1.15% | **+0.81%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +0.72% | **+0.39%** |

## 2. $100 Live Portfolio

- 残高: **$101.34** / 初期 $100.00 (+1.34%)
- 確定トレード: 19件 (TP 6 / SL 11 / EXP 2)
- 最新: TAG/USDT:USDT TP_HIT PnL +8.00% 残高後 $101.34
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$100.00** / 初期 $100.00 (+0.00%)
- 確定: 0件 (Win 0 / Loss 0 / Flat 0) / skip 0件
- 成長率目線: 平均log +0.000000 / 幾何平均 +0.000% per trade / maxDD +0.00%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 状態: 新しい$100口座として開始済み。開始後に閉じたシャドウトレードから反映します。

## 4. Latest Market Context

- 更新: 2026-05-06T08:42:31.379925+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.41% price=81665.9
- Funnel: target 767 → liquid 198 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 81.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| IO/USDT:USDT | +53.23% | $9,043,934.77 |
| ZEC/USDT:USDT | +39.42% | $725,943,753.19 |
| B3/USDT:USDT | +30.76% | $1,457,816.34 |
| STORJ/USDT:USDT | +28.92% | $2,538,644.07 |
| DASH/USDT:USDT | +26.77% | $35,883,939.65 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| NEAR/USDT:USDT | below_1h_threshold | +4.49% | +4.08% |
| ZRO/USDT:USDT | below_1h_threshold | +3.61% | +3.20% |
| STRK/USDT:USDT | below_1h_threshold | +3.34% | +2.93% |
| LAB/USDT:USDT | below_1h_threshold | +3.20% | +2.79% |
| XPL/USDT:USDT | below_1h_threshold | +3.16% | +2.75% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
