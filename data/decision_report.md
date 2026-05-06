# Decision Report

- generated_at: 2026-05-06T08:29:27.568373+00:00
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

- 更新: 2026-05-06T08:27:25.121780+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.22% price=81509.9
- Funnel: target 768 → liquid 199 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 80.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| IO/USDT:USDT | +59.77% | $8,320,490.93 |
| ZEC/USDT:USDT | +38.30% | $718,083,048.83 |
| B3/USDT:USDT | +30.90% | $1,454,320.68 |
| STORJ/USDT:USDT | +29.52% | $2,510,288.05 |
| FHE/USDT:USDT | +23.90% | $28,741,637.07 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TAG/USDT:USDT | below_1h_threshold | +3.92% | +3.70% |
| FILECOIN/USDT:USDT | below_1h_threshold | +3.27% | +3.05% |
| NEAR/USDT:USDT | below_1h_threshold | +2.80% | +2.58% |
| FHE/USDT:USDT | below_1h_threshold | +2.71% | +2.50% |
| S/USDT:USDT | below_1h_threshold | +2.55% | +2.33% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
