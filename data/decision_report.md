# Decision Report

- generated_at: 2026-07-22T03:11:26.689631+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9242**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=9242, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.59%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.59% | **-1.59%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 3/20 | 15.0% | +7.23% | **+1.08%** |
| LIMIT_6PCT | 8/20 | 40.0% | +0.48% | **+0.19%** |
| LIMIT_FIB1618 | 3/20 | 15.0% | +1.23% | **+0.18%** |
| LIMIT_7PCT | 6/20 | 30.0% | +0.58% | **+0.17%** |
| LIMIT_8PCT | 4/20 | 20.0% | -0.09% | **-0.02%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +3.89% | **+3.70%** |
| MARKET_LONG | 20/20 | 100.0% | +3.17% | **+3.17%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +3.89% | **+2.92%** |
| LIMIT_3PCT_LONG | 9/20 | 45.0% | +2.49% | **+1.12%** |
| LIMIT_ATR_LONG | 7/20 | 35.0% | +1.39% | **+0.49%** |

## 2. $100 Live Portfolio

- 残高: **$104.85** / 初期 $100.00 (+4.85%)
- 確定トレード: 131件 (TP 44 / SL 82 / EXP 5)
- 最新: NIGHT/USDT:USDT SL_HIT PnL -4.00% 残高後 $104.85
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$419.29** / 初期 $100.00 (+319.29%)
- 確定: 3250件 (Win 1021 / Loss 1039 / Flat 1190) / skip 2553件
- 成長率目線: 平均log +0.000441 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BNCSTOCK/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account +0.00% 残高後 $419.29

## 4. Robust Adaptive DryRun ($100)

- 残高: **$131.28** / 初期 $100.00 (+31.28%)
- 確定: 1159件 (Win 312 / Loss 252 / Flat 595) / skip 1494件
- 成長率目線: 平均log +0.000235 / 幾何平均 +0.023% per trade / maxDD +3.89%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1552 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: RIF/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $131.28

## 5. Causal Adaptive DryRun ($100)

- 残高: **$101.88** / 初期 $100.00 (+1.88%)
- 確定: 386件 (Win 131 / Loss 158 / Flat 97) / pending 5件 / skip 325件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000293 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: LAB/USDT:USDT `LIMIT_7PCT` SL_HIT account +0.12% 残高後 $101.88

## 6. Latest Market Context

- 更新: 2026-07-22T03:11:17.455677+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.10% price=66215.0
- Funnel: target 885 → liquid 173 → pre 50 → checked 50 → surge 3 → strict 1
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 83.1 >= 65=1, 4h RSI 78.8 >= 65=1
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| JIMOTHY/USDT:USDT | +45.05% | $4,134,239.11 |
| PONS/USDT:USDT | +20.39% | $2,144,027.61 |
| SMCISTOCK/USDT:USDT | +18.59% | $3,761,869.15 |
| LAB/USDT:USDT | +18.02% | $6,238,979.95 |
| FWDISTOCK/USDT:USDT | +15.94% | $4,174,937.38 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| FWDISTOCK/USDT:USDT | below_1h_threshold | +2.76% | +2.86% |
| B/USDT:USDT | below_1h_threshold | +2.26% | +2.36% |
| TLM/USDT:USDT | below_1h_threshold | +1.24% | +1.35% |
| MYX/USDT:USDT | below_1h_threshold | +1.21% | +1.32% |
| BEAT/USDT:USDT | below_1h_threshold | +1.08% | +1.19% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
