# Decision Report

- generated_at: 2026-07-22T04:31:28.695308+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9251**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=9251, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.59%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.59% | **-1.59%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 3/20 | 15.0% | +6.38% | **+0.96%** |
| LIMIT_8PCT | 5/20 | 25.0% | +2.21% | **+0.55%** |
| LIMIT_7PCT | 6/20 | 30.0% | +1.71% | **+0.51%** |
| LIMIT_9PCT | 3/20 | 15.0% | +1.81% | **+0.27%** |
| LIMIT_FIB1618 | 3/20 | 15.0% | +1.23% | **+0.18%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +3.66% | **+3.30%** |
| MARKET_LONG | 20/20 | 100.0% | +2.97% | **+2.97%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +3.33% | **+2.00%** |
| LIMIT_ATR_LONG | 7/20 | 35.0% | +1.52% | **+0.53%** |
| LIMIT_3PCT_LONG | 7/20 | 35.0% | +1.03% | **+0.36%** |

## 2. $100 Live Portfolio

- 残高: **$104.85** / 初期 $100.00 (+4.85%)
- 確定トレード: 131件 (TP 44 / SL 82 / EXP 5)
- 最新: NIGHT/USDT:USDT SL_HIT PnL -4.00% 残高後 $104.85
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$424.60** / 初期 $100.00 (+324.60%)
- 確定: 3252件 (Win 1023 / Loss 1039 / Flat 1190) / skip 2560件
- 成長率目線: 平均log +0.000445 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: LAB/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.63% 残高後 $424.60

## 4. Robust Adaptive DryRun ($100)

- 残高: **$131.28** / 初期 $100.00 (+31.28%)
- 確定: 1159件 (Win 312 / Loss 252 / Flat 595) / skip 1503件
- 成長率目線: 平均log +0.000235 / 幾何平均 +0.023% per trade / maxDD +3.89%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.2006 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: RIF/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $131.28

## 5. Causal Adaptive DryRun ($100)

- 残高: **$102.73** / 初期 $100.00 (+2.73%)
- 確定: 395件 (Win 137 / Loss 161 / Flat 97) / pending 4件 / skip 326件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000443 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: LAB/USDT:USDT `MARKET_LONG` EXPIRED account +0.17% 残高後 $102.73

## 6. Latest Market Context

- 更新: 2026-07-22T04:31:17.558121+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.21% price=66315.4
- Funnel: target 885 → liquid 177 → pre 50 → checked 50 → surge 2 → strict 2
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| JIMOTHY/USDT:USDT | +48.05% | $4,249,678.71 |
| LAB/USDT:USDT | +42.01% | $8,446,581.26 |
| BANK/USDT:USDT | +21.65% | $123,161,145.72 |
| SMCISTOCK/USDT:USDT | +19.38% | $3,919,473.70 |
| FWDISTOCK/USDT:USDT | +12.82% | $4,373,432.46 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BEAT/USDT:USDT | below_1h_threshold | +2.60% | +2.39% |
| US/USDT:USDT | below_1h_threshold | +2.23% | +2.02% |
| UB/USDT:USDT | below_1h_threshold | +1.52% | +1.31% |
| JIMOTHY/USDT:USDT | below_1h_threshold | +1.27% | +1.06% |
| ENA/USDT:USDT | below_1h_threshold | +1.01% | +0.80% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
