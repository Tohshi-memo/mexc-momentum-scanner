# Decision Report

- generated_at: 2026-07-22T03:36:24.224790+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9246**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=9246, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.99%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.99% | **-0.99%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 3/20 | 15.0% | +7.23% | **+1.08%** |
| LIMIT_FIB1618 | 3/20 | 15.0% | +1.23% | **+0.18%** |
| LIMIT_7PCT | 6/20 | 30.0% | +0.58% | **+0.17%** |
| LIMIT_8PCT | 5/20 | 25.0% | +0.67% | **+0.17%** |
| LIMIT_9PCT | 3/20 | 15.0% | -1.06% | **-0.16%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +2.97% | **+2.97%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +3.16% | **+2.85%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +2.62% | **+1.70%** |
| LIMIT_ATR_LONG | 8/20 | 40.0% | +0.99% | **+0.40%** |
| LIMIT_FIB1272_LONG | 2/20 | 10.0% | +3.51% | **+0.35%** |

## 2. $100 Live Portfolio

- 残高: **$104.85** / 初期 $100.00 (+4.85%)
- 確定トレード: 131件 (TP 44 / SL 82 / EXP 5)
- 最新: NIGHT/USDT:USDT SL_HIT PnL -4.00% 残高後 $104.85
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$419.29** / 初期 $100.00 (+319.29%)
- 確定: 3250件 (Win 1021 / Loss 1039 / Flat 1190) / skip 2557件
- 成長率目線: 平均log +0.000441 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BNCSTOCK/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account +0.00% 残高後 $419.29

## 4. Robust Adaptive DryRun ($100)

- 残高: **$131.28** / 初期 $100.00 (+31.28%)
- 確定: 1159件 (Win 312 / Loss 252 / Flat 595) / skip 1498件
- 成長率目線: 平均log +0.000235 / 幾何平均 +0.023% per trade / maxDD +3.89%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1428 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: RIF/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $131.28

## 5. Causal Adaptive DryRun ($100)

- 残高: **$102.39** / 初期 $100.00 (+2.39%)
- 確定: 390件 (Win 134 / Loss 159 / Flat 97) / pending 5件 / skip 325件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000397 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BANK/USDT:USDT `MARKET_LONG` TP_HIT account +0.34% 残高後 $102.39

## 6. Latest Market Context

- 更新: 2026-07-22T03:36:17.313156+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.11% price=66208.5
- Funnel: target 885 → liquid 175 → pre 50 → checked 50 → surge 4 → strict 2
- Surge前reject: below_1h_threshold=46, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 82.9 >= 65=1, 4h RSI 78.4 >= 65=1
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| JIMOTHY/USDT:USDT | +38.49% | $4,190,546.66 |
| BANK/USDT:USDT | +20.05% | $121,216,904.30 |
| PONS/USDT:USDT | +19.90% | $2,170,932.12 |
| SMCISTOCK/USDT:USDT | +19.03% | $3,810,795.14 |
| LAB/USDT:USDT | +17.88% | $6,724,993.37 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TLM/USDT:USDT | below_1h_threshold | +3.37% | +3.49% |
| FWDISTOCK/USDT:USDT | below_1h_threshold | +2.76% | +2.87% |
| RE/USDT:USDT | below_1h_threshold | +2.31% | +2.42% |
| B/USDT:USDT | below_1h_threshold | +2.09% | +2.21% |
| MYX/USDT:USDT | below_1h_threshold | +1.88% | +1.99% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
