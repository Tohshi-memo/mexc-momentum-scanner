# Decision Report

- generated_at: 2026-10-23T15:56:42.543292+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **17241**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=17241, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=-3.40%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -3.40% | **-3.40%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 12/20 | 60.0% | +0.98% | **+0.59%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +4.08% | **+0.41%** |
| LIMIT_7PCT | 10/20 | 50.0% | +0.80% | **+0.40%** |
| LIMIT_9PCT | 7/20 | 35.0% | +1.14% | **+0.40%** |
| LIMIT_8PCT | 7/20 | 35.0% | +1.14% | **+0.40%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +4.08% | **+3.87%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +4.89% | **+3.42%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | +5.65% | **+3.11%** |
| LIMIT_3PCT_LONG | 9/20 | 45.0% | +5.33% | **+2.40%** |
| LIMIT_4PCT_LONG | 7/20 | 35.0% | +6.29% | **+2.20%** |

## 2. $100 Live Portfolio

- 残高: **$121.49** / 初期 $100.00 (+21.49%)
- 確定トレード: 250件 (TP 92 / SL 150 / EXP 8)
- 最新: MSTRSTOCK/USDT:USDT EXPIRED PnL +0.27% 残高後 $121.49
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,310.72** / 初期 $100.00 (+1210.72%)
- 確定: 6553件 (Win 1902 / Loss 2094 / Flat 2557) / skip 7249件
- 成長率目線: 平均log +0.000393 / 幾何平均 +0.039% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: UNITREE/USDT:USDT `MARKET` SL_HIT account -0.50% 残高後 $1,310.72

## 4. Robust Adaptive DryRun ($100)

- 残高: **$289.78** / 初期 $100.00 (+189.78%)
- 確定: 3905件 (Win 1071 / Loss 908 / Flat 1926) / skip 6747件
- 成長率目線: 平均log +0.000272 / 幾何平均 +0.027% per trade / maxDD +4.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.2016 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: JCT/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.43% 残高後 $289.78

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 5402件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000518 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-23T15:56:19.640924+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.25% price=81543.9
- Funnel: target 1088 → liquid 170 → pre 50 → checked 50 → surge 4 → strict 1
- Surge前reject: below_1h_threshold=46, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 92.6 >= 65=1, 4h RSI 84.7 >= 65=1, 4h RSI 72.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| IRYS/USDT:USDT | +194.47% | $35,538,678.78 |
| BIRB/USDT:USDT | +75.09% | $2,636,834.65 |
| BTR/USDT:USDT | +45.77% | $16,015,528.94 |
| UNITREE/USDT:USDT | +21.83% | $6,133,536.20 |
| DNA/USDT:USDT | +14.50% | $5,366,240.62 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BTR/USDT:USDT | below_1h_threshold | +2.76% | +3.01% |
| MVLL/USDT:USDT | below_1h_threshold | +2.41% | +2.66% |
| DNA/USDT:USDT | below_1h_threshold | +1.81% | +2.06% |
| AKE/USDT:USDT | below_1h_threshold | +1.36% | +1.61% |
| MRVLSTOCK/USDT:USDT | below_1h_threshold | +1.26% | +1.52% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
