# Decision Report

- generated_at: 2026-07-19T14:56:14.563353+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9048**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=9048, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.39%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.39% | **-0.39%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 7/20 | 35.0% | +4.15% | **+1.45%** |
| LIMIT_2PCT | 18/20 | 90.0% | +1.25% | **+1.13%** |
| LIMIT_5PCT | 7/20 | 35.0% | +2.97% | **+1.04%** |
| LIMIT_6PCT | 2/20 | 10.0% | +4.94% | **+0.49%** |
| LIMIT_3PCT | 15/20 | 75.0% | +0.63% | **+0.47%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 5/20 | 25.0% | +4.44% | **+1.11%** |
| LIMIT_ATR_LONG | 7/20 | 35.0% | +2.46% | **+0.86%** |
| LIMIT_9PCT_LONG | 6/20 | 30.0% | +2.85% | **+0.85%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +2.29% | **+0.80%** |
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +1.56% | **+0.55%** |

## 2. $100 Live Portfolio

- 残高: **$110.80** / 初期 $100.00 (+10.80%)
- 確定トレード: 117件 (TP 43 / SL 69 / EXP 5)
- 最新: SKYAI/USDT:USDT EXPIRED PnL +0.79% 残高後 $110.80
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$401.33** / 初期 $100.00 (+301.33%)
- 確定: 3110件 (Win 976 / Loss 992 / Flat 1142) / skip 2499件
- 成長率目線: 平均log +0.000447 / 幾何平均 +0.045% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ESPORTS/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $401.33

## 4. Robust Adaptive DryRun ($100)

- 残高: **$127.17** / 初期 $100.00 (+27.17%)
- 確定: 1009件 (Win 261 / Loss 212 / Flat 536) / skip 1450件
- 成長率目線: 平均log +0.000238 / 幾何平均 +0.024% per trade / maxDD +3.89%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0998 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ESPORTS/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $127.17

## 5. Causal Adaptive DryRun ($100)

- 残高: **$101.02** / 初期 $100.00 (+1.02%)
- 確定: 248件 (Win 85 / Loss 123 / Flat 40) / pending 6件 / skip 267件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000421 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: B/USDT:USDT `MARKET_LONG` EXPIRED account +0.17% 残高後 $101.02

## 6. Latest Market Context

- 更新: 2026-07-19T14:56:08.880481+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.19% price=64576.4
- Funnel: target 885 → liquid 127 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 78.9 >= 65=1, 4h RSI 91.1 >= 65=1
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BANK/USDT:USDT | +162.27% | $46,066,019.85 |
| TLM/USDT:USDT | +79.22% | $9,132,282.03 |
| B/USDT:USDT | +58.93% | $34,225,672.61 |
| TAG/USDT:USDT | +23.09% | $4,938,370.77 |
| PI/USDT:USDT | +17.16% | $4,753,404.83 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ANSEM/USDT:USDT | below_1h_threshold | +4.69% | +4.50% |
| TLM/USDT:USDT | below_1h_threshold | +4.63% | +4.44% |
| PI/USDT:USDT | below_1h_threshold | +3.41% | +3.22% |
| KAITO/USDT:USDT | below_1h_threshold | +2.25% | +2.06% |
| ALLO/USDT:USDT | below_1h_threshold | +2.10% | +1.91% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
