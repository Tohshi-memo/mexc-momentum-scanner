# Decision Report

- generated_at: 2026-07-18T16:41:25.861662+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8957**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=8957, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.00%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.00% | **-1.00%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 10/20 | 50.0% | +2.08% | **+1.04%** |
| LIMIT_8PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +3.83% | **+0.38%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.27% | **+0.34%** |
| LIMIT_6PCT | 6/20 | 30.0% | +0.94% | **+0.28%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +2.40% | **+1.56%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +1.53% | **+1.22%** |
| LIMIT_BB3S_LONG | 3/7 | 42.9% | +2.47% | **+1.06%** |
| LIMIT_5PCT_LONG | 10/20 | 50.0% | +2.08% | **+1.04%** |
| LIMIT_6PCT_LONG | 8/20 | 40.0% | +2.47% | **+0.99%** |

## 2. $100 Live Portfolio

- 残高: **$110.69** / 初期 $100.00 (+10.69%)
- 確定トレード: 116件 (TP 43 / SL 69 / EXP 4)
- 最新: B/USDT:USDT SL_HIT PnL -3.30% 残高後 $110.69
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$358.77** / 初期 $100.00 (+258.77%)
- 確定: 3049件 (Win 946 / Loss 973 / Flat 1130) / skip 2469件
- 成長率目線: 平均log +0.000419 / 幾何平均 +0.042% per trade / maxDD +8.13%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: B/USDT:USDT `MARKET` SL_HIT account -0.50% 残高後 $358.77

## 4. Robust Adaptive DryRun ($100)

- 残高: **$114.29** / 初期 $100.00 (+14.29%)
- 確定: 918件 (Win 224 / Loss 187 / Flat 507) / skip 1450件
- 成長率目線: 平均log +0.000146 / 幾何平均 +0.015% per trade / maxDD +3.89%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0741 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BANK/USDT:USDT `LIMIT_2PCT_LONG` TP_HIT account +0.69% 残高後 $114.29

## 5. Causal Adaptive DryRun ($100)

- 残高: **$98.89** / 初期 $100.00 (-1.11%)
- 確定: 195件 (Win 61 / Loss 107 / Flat 27) / pending 1件 / skip 234件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000318 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ALLO/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $98.89

## 6. Latest Market Context

- 更新: 2026-07-18T16:41:15.178601+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.02% price=64100.1
- Funnel: target 885 → liquid 142 → pre 50 → checked 50 → surge 3 → strict 1
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 81.5 >= 65=1, 4h RSI 81.6 >= 65=1
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BANK/USDT:USDT | +38.85% | $14,883,806.16 |
| ESPORTS/USDT:USDT | +18.11% | $16,707,534.93 |
| AVAAI/USDT:USDT | +5.40% | $1,057,393.54 |
| BILL/USDT:USDT | +4.10% | $3,313,911.34 |
| LAB/USDT:USDT | +4.02% | $6,664,123.73 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BILL/USDT:USDT | below_1h_threshold | +4.31% | +4.30% |
| LAB/USDT:USDT | below_1h_threshold | +4.02% | +4.01% |
| ROAM/USDT:USDT | below_1h_threshold | +2.50% | +2.49% |
| TAG/USDT:USDT | below_1h_threshold | +1.78% | +1.76% |
| B/USDT:USDT | below_1h_threshold | +1.77% | +1.75% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
