# Decision Report

- generated_at: 2026-08-22T01:56:30.784288+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12291**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=12291, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-2.27%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.27% | **-2.27%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 6/20 | 30.0% | +2.27% | **+0.68%** |
| LIMIT_5PCT | 9/20 | 45.0% | +1.42% | **+0.64%** |
| LIMIT_6PCT | 8/20 | 40.0% | +1.18% | **+0.47%** |
| LIMIT_ATR | 15/20 | 75.0% | +0.39% | **+0.29%** |
| LIMIT_10PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +4.38% | **+4.38%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +4.82% | **+3.62%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +4.62% | **+2.54%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +2.90% | **+2.46%** |
| LIMIT_4PCT_LONG | 9/20 | 45.0% | +4.50% | **+2.02%** |

## 2. $100 Live Portfolio

- 残高: **$121.04** / 初期 $100.00 (+21.04%)
- 確定トレード: 190件 (TP 72 / SL 113 / EXP 5)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.04
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$697.73** / 初期 $100.00 (+597.73%)
- 確定: 4409件 (Win 1351 / Loss 1441 / Flat 1617) / skip 4443件
- 成長率目線: 平均log +0.000441 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BASECAT/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $697.73

## 4. Robust Adaptive DryRun ($100)

- 残高: **$154.35** / 初期 $100.00 (+54.35%)
- 確定: 1897件 (Win 522 / Loss 454 / Flat 921) / skip 3805件
- 成長率目線: 平均log +0.000229 / 幾何平均 +0.023% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.2139 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BASECAT/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $154.35

## 5. Causal Adaptive DryRun ($100)

- 残高: **$118.18** / 初期 $100.00 (+18.18%)
- 確定: 1840件 (Win 546 / Loss 695 / Flat 599) / pending 5件 / skip 1921件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000522 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BASECAT/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.26% 残高後 $118.18

## 6. Latest Market Context

- 更新: 2026-08-22T01:56:18.758502+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.05% price=77875.2
- Funnel: target 1018 → liquid 218 → pre 50 → checked 50 → surge 3 → strict 0
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 88.5 >= 65=1, 4h RSI 95.2 >= 65=1, 4h RSI 74.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BASECAT/USDT:USDT | +305.15% | $3,797,875.19 |
| CATE/USDT:USDT | +56.53% | $12,187,866.91 |
| AGI/USDT:USDT | +30.79% | $1,745,345.21 |
| RE/USDT:USDT | +22.25% | $7,154,786.42 |
| ZEC/USDT:USDT | +19.95% | $300,204,557.12 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ZEN/USDT:USDT | below_1h_threshold | +4.81% | +4.86% |
| SKYAI/USDT:USDT | below_1h_threshold | +3.24% | +3.30% |
| CRO/USDT:USDT | below_1h_threshold | +3.12% | +3.17% |
| AGI/USDT:USDT | below_1h_threshold | +2.76% | +2.82% |
| TRB/USDT:USDT | below_1h_threshold | +2.10% | +2.15% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
