# Decision Report

- generated_at: 2026-08-08T15:16:20.280428+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10857**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=10857, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-2.06%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.06% | **-2.06%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 3/20 | 15.0% | +8.00% | **+1.20%** |
| LIMIT_6PCT | 5/20 | 25.0% | +4.33% | **+1.08%** |
| LIMIT_7PCT | 3/20 | 15.0% | +6.27% | **+0.94%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_4PCT | 15/20 | 75.0% | +1.07% | **+0.80%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +4.73% | **+2.60%** |
| LIMIT_BB3S_LONG | 3/3 | 100.0% | +2.37% | **+2.37%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +3.24% | **+1.95%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +1.82% | **+1.73%** |
| LIMIT_5PCT_LONG | 8/20 | 40.0% | +3.99% | **+1.60%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 176件 (TP 67 / SL 104 / EXP 5)
- 最新: AAOISTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$640.26** / 初期 $100.00 (+540.26%)
- 確定: 3858件 (Win 1214 / Loss 1253 / Flat 1391) / skip 3560件
- 成長率目線: 平均log +0.000481 / 幾何平均 +0.048% per trade / maxDD +8.13%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ACE/USDT:USDT `LIMIT_ATR_LONG` EXPIRED account +0.94% 残高後 $640.26

## 4. Robust Adaptive DryRun ($100)

- 残高: **$142.00** / 初期 $100.00 (+42.00%)
- 確定: 1510件 (Win 424 / Loss 360 / Flat 726) / skip 2758件
- 成長率目線: 平均log +0.000232 / 幾何平均 +0.023% per trade / maxDD +3.96%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0659 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: JIMOTHY/USDT:USDT `LIMIT_5PCT` SL_HIT account -0.35% 残高後 $142.00

## 5. Causal Adaptive DryRun ($100)

- 残高: **$118.83** / 初期 $100.00 (+18.83%)
- 確定: 1225件 (Win 386 / Loss 469 / Flat 370) / pending 6件 / skip 1099件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000311 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ACE/USDT:USDT `LIMIT_10PCT_LONG` EXPIRED account +0.00% 残高後 $118.83

## 6. Latest Market Context

- 更新: 2026-08-08T15:16:11.778221+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.03% price=65079.3
- Funnel: target 961 → liquid 158 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 92.6 >= 65=1, 4h RSI 80.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| JIMOTHY/USDT:USDT | +257.87% | $12,014,917.63 |
| TUT/USDT:USDT | +83.90% | $11,706,925.95 |
| CAT/USDT:USDT | +61.67% | $1,052,868.60 |
| BLUAI/USDT:USDT | +40.78% | $4,542,256.37 |
| BEAT/USDT:USDT | +36.38% | $32,320,466.83 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SKYAI/USDT:USDT | below_1h_threshold | +4.15% | +4.18% |
| BLUAI/USDT:USDT | below_1h_threshold | +3.00% | +3.03% |
| TUT/USDT:USDT | below_1h_threshold | +2.54% | +2.57% |
| BEAT/USDT:USDT | below_1h_threshold | +1.76% | +1.79% |
| KGEN/USDT:USDT | below_1h_threshold | +1.28% | +1.31% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
