# Decision Report

- generated_at: 2026-10-23T07:51:37.259664+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **17202**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=17202, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=-0.76%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.76% | **-0.76%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 2/20 | 10.0% | +5.85% | **+0.59%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +4.33% | **+0.43%** |
| LIMIT_6PCT | 4/20 | 20.0% | +1.89% | **+0.38%** |
| LIMIT_FIB1272 | 10/20 | 50.0% | +0.73% | **+0.37%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +1.71% | **+1.37%** |
| MARKET_LONG | 20/20 | 100.0% | +1.26% | **+1.26%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | +3.73% | **+0.37%** |
| LIMIT_FIB1272_LONG | 7/20 | 35.0% | +1.02% | **+0.36%** |
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +0.43% | **+0.22%** |

## 2. $100 Live Portfolio

- 残高: **$121.49** / 初期 $100.00 (+21.49%)
- 確定トレード: 250件 (TP 92 / SL 150 / EXP 8)
- 最新: MSTRSTOCK/USDT:USDT EXPIRED PnL +0.27% 残高後 $121.49
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,310.72** / 初期 $100.00 (+1210.72%)
- 確定: 6553件 (Win 1902 / Loss 2094 / Flat 2557) / skip 7210件
- 成長率目線: 平均log +0.000393 / 幾何平均 +0.039% per trade / maxDD +8.46%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: UNITREE/USDT:USDT `MARKET` SL_HIT account -0.50% 残高後 $1,310.72

## 4. Robust Adaptive DryRun ($100)

- 残高: **$276.15** / 初期 $100.00 (+176.15%)
- 確定: 3875件 (Win 1057 / Loss 901 / Flat 1917) / skip 6738件
- 成長率目線: 平均log +0.000262 / 幾何平均 +0.026% per trade / maxDD +4.13%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: IRYS/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $276.15

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 5365件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000117 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-23T07:51:19.415411+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.33% price=81581.9
- Funnel: target 1083 → liquid 173 → pre 50 → checked 50 → surge 4 → strict 2
- Surge前reject: below_1h_threshold=46, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 81.1 >= 65=1, 4h RSI 86.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| IRYS/USDT:USDT | +46.04% | $4,300,461.58 |
| BTR/USDT:USDT | +40.63% | $14,215,646.48 |
| DNA/USDT:USDT | +33.43% | $4,475,762.32 |
| UNITREE/USDT:USDT | +21.61% | $3,039,741.68 |
| ZHIPUSTOCK/USDT:USDT | +10.45% | $1,962,595.08 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ZHIPUSTOCK/USDT:USDT | below_1h_threshold | +2.26% | +2.59% |
| AGT/USDT:USDT | below_1h_threshold | +1.93% | +2.26% |
| KIOXIASTOCK/USDT:USDT | below_1h_threshold | +1.38% | +1.71% |
| BEAT/USDT:USDT | below_1h_threshold | +1.20% | +1.53% |
| GRASS/USDT:USDT | below_1h_threshold | +1.04% | +1.37% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
