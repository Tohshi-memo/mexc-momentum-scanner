# Decision Report

- generated_at: 2026-07-22T04:41:17.242920+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9252**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=9252, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.59%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.59% | **-1.59%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 4/20 | 20.0% | +3.77% | **+0.75%** |
| LIMIT_7PCT | 5/20 | 25.0% | +2.85% | **+0.71%** |
| LIMIT_10PCT | 2/20 | 10.0% | +5.58% | **+0.56%** |
| LIMIT_9PCT | 2/20 | 10.0% | +4.71% | **+0.47%** |
| LIMIT_FIB1618 | 3/20 | 15.0% | +1.23% | **+0.18%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +3.00% | **+2.70%** |
| MARKET_LONG | 20/20 | 100.0% | +2.37% | **+2.37%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +2.33% | **+1.40%** |
| LIMIT_FIB1272_LONG | 3/20 | 15.0% | +3.72% | **+0.56%** |
| LIMIT_8PCT_LONG | 5/20 | 25.0% | +1.60% | **+0.40%** |

## 2. $100 Live Portfolio

- 残高: **$104.85** / 初期 $100.00 (+4.85%)
- 確定トレード: 131件 (TP 44 / SL 82 / EXP 5)
- 最新: NIGHT/USDT:USDT SL_HIT PnL -4.00% 残高後 $104.85
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$422.48** / 初期 $100.00 (+322.48%)
- 確定: 3253件 (Win 1023 / Loss 1040 / Flat 1190) / skip 2560件
- 成長率目線: 平均log +0.000443 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: LAB/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $422.48

## 4. Robust Adaptive DryRun ($100)

- 残高: **$131.28** / 初期 $100.00 (+31.28%)
- 確定: 1159件 (Win 312 / Loss 252 / Flat 595) / skip 1504件
- 成長率目線: 平均log +0.000235 / 幾何平均 +0.023% per trade / maxDD +3.89%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1850 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: RIF/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $131.28

## 5. Causal Adaptive DryRun ($100)

- 残高: **$102.55** / 初期 $100.00 (+2.55%)
- 確定: 396件 (Win 137 / Loss 162 / Flat 97) / pending 3件 / skip 326件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000404 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: LAB/USDT:USDT `MARKET_LONG` SL_HIT account -0.17% 残高後 $102.55

## 6. Latest Market Context

- 更新: 2026-07-22T04:41:11.794177+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.27% price=66354.6
- Funnel: target 885 → liquid 177 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| JIMOTHY/USDT:USDT | +45.73% | $4,267,973.47 |
| LAB/USDT:USDT | +30.61% | $9,323,317.58 |
| BANK/USDT:USDT | +20.73% | $124,024,983.17 |
| SMCISTOCK/USDT:USDT | +18.79% | $3,928,375.29 |
| RE/USDT:USDT | +13.25% | $2,130,245.31 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| UB/USDT:USDT | below_1h_threshold | +2.68% | +2.41% |
| US/USDT:USDT | below_1h_threshold | +2.26% | +1.99% |
| BEAT/USDT:USDT | below_1h_threshold | +1.81% | +1.54% |
| NIGHT/USDT:USDT | below_1h_threshold | +1.50% | +1.23% |
| LAB/USDT:USDT | below_1h_threshold | +1.31% | +1.04% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
