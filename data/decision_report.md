# Decision Report

- generated_at: 2026-07-22T05:36:15.529055+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9255**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=9255, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.77%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.77% | **-1.77%** |

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
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +3.10% | **+2.63%** |
| MARKET_LONG | 20/20 | 100.0% | +2.35% | **+2.35%** |
| LIMIT_2PCT_LONG | 10/20 | 50.0% | +2.58% | **+1.29%** |
| LIMIT_8PCT_LONG | 4/20 | 20.0% | +2.00% | **+0.40%** |
| LIMIT_BB3S_LONG | 2/3 | 66.7% | +0.59% | **+0.39%** |

## 2. $100 Live Portfolio

- 残高: **$104.85** / 初期 $100.00 (+4.85%)
- 確定トレード: 131件 (TP 44 / SL 82 / EXP 5)
- 最新: NIGHT/USDT:USDT SL_HIT PnL -4.00% 残高後 $104.85
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$425.15** / 初期 $100.00 (+325.15%)
- 確定: 3254件 (Win 1024 / Loss 1040 / Flat 1190) / skip 2562件
- 成長率目線: 平均log +0.000445 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AKE/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.63% 残高後 $425.15

## 4. Robust Adaptive DryRun ($100)

- 残高: **$131.28** / 初期 $100.00 (+31.28%)
- 確定: 1159件 (Win 312 / Loss 252 / Flat 595) / skip 1507件
- 成長率目線: 平均log +0.000235 / 幾何平均 +0.023% per trade / maxDD +3.89%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1956 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: RIF/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $131.28

## 5. Causal Adaptive DryRun ($100)

- 残高: **$102.55** / 初期 $100.00 (+2.55%)
- 確定: 397件 (Win 137 / Loss 162 / Flat 98) / pending 3件 / skip 326件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000433 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: SMCISTOCK/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $102.55

## 6. Latest Market Context

- 更新: 2026-07-22T05:36:07.543711+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.42% price=66069.6
- Funnel: target 885 → liquid 175 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LAB/USDT:USDT | +39.95% | $10,518,575.61 |
| JIMOTHY/USDT:USDT | +30.71% | $4,244,162.69 |
| SMCISTOCK/USDT:USDT | +18.55% | $4,029,353.85 |
| RE/USDT:USDT | +17.35% | $2,461,889.57 |
| BANK/USDT:USDT | +15.41% | $124,034,837.75 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AKE/USDT:USDT | below_1h_threshold | +3.24% | +3.66% |
| BILL/USDT:USDT | below_1h_threshold | +2.88% | +3.31% |
| RE/USDT:USDT | below_1h_threshold | +2.03% | +2.45% |
| ESPORTS/USDT:USDT | below_1h_threshold | +1.37% | +1.80% |
| BOTSTOCK/USDT:USDT | below_1h_threshold | +1.32% | +1.75% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
