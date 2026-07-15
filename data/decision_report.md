# Decision Report

- generated_at: 2026-07-15T21:11:21.144527+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8766**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.88% / filled 20/20。**
- 全期間 MARKET基準: n=8766, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=+1.88%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.88% | **+1.88%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.88% | **+1.88%** |
| LIMIT_1PCT | 19/20 | 95.0% | +1.83% | **+1.73%** |
| LIMIT_ATR | 14/20 | 70.0% | +2.14% | **+1.50%** |
| LIMIT_2PCT | 16/20 | 80.0% | +1.86% | **+1.49%** |
| LIMIT_3PCT | 12/20 | 60.0% | +1.26% | **+0.76%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT_LONG | 11/20 | 55.0% | +0.37% | **+0.20%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | -0.58% | **-0.15%** |
| LIMIT_10PCT_LONG | 4/20 | 20.0% | -1.00% | **-0.20%** |
| MARKET_LONG | 20/20 | 100.0% | -0.49% | **-0.49%** |
| LIMIT_BB3S_LONG | 6/6 | 100.0% | -0.55% | **-0.55%** |

## 2. $100 Live Portfolio

- 残高: **$103.22** / 初期 $100.00 (+3.22%)
- 確定トレード: 99件 (TP 34 / SL 63 / EXP 2)
- 最新: LAB/USDT:USDT SL_HIT PnL -4.00% 残高後 $103.22
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$341.18** / 初期 $100.00 (+241.18%)
- 確定: 2885件 (Win 903 / Loss 939 / Flat 1043) / skip 2442件
- 成長率目線: 平均log +0.000425 / 幾何平均 +0.043% per trade / maxDD +8.13%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ROAM/USDT:USDT `LIMIT_BB3S_LONG` SL_HIT account -0.50% 残高後 $341.18

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.12** / 初期 $100.00 (+6.12%)
- 確定: 730件 (Win 168 / Loss 168 / Flat 394) / skip 1447件
- 成長率目線: 平均log +0.000081 / 幾何平均 +0.008% per trade / maxDD +3.89%
- 次の候補: `LIMIT_7PCT` (selected_by_robust_growth_score) / robust_score +0.1110 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ROAM/USDT:USDT `LIMIT_7PCT` TP_HIT account +0.69% 残高後 $106.12

## 5. Causal Adaptive DryRun ($100)

- 残高: **$98.49** / 初期 $100.00 (-1.51%)
- 確定: 64件 (Win 19 / Loss 41 / Flat 4) / pending 0件 / skip 176件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_7PCT` (selected_by_causal_log_growth) / causal_score +0.000279 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: XEC/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account -0.09% 残高後 $98.49

## 6. Latest Market Context

- 更新: 2026-07-15T21:11:13.604677+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.10% price=64871.2
- Funnel: target 871 → liquid 169 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 90.9 >= 65=1
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ROAM/USDT:USDT | +94.20% | $3,781,353.89 |
| SKL/USDT:USDT | +13.78% | $1,645,564.18 |
| CAP/USDT:USDT | +13.16% | $1,340,108.48 |
| HOME/USDT:USDT | +10.08% | $1,057,407.64 |
| SNXX/USDT:USDT | +9.60% | $1,325,990.48 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| DEXE/USDT:USDT | below_1h_threshold | +3.12% | +3.22% |
| LDO/USDT:USDT | below_1h_threshold | +1.28% | +1.39% |
| ONDO/USDT:USDT | below_1h_threshold | +0.84% | +0.94% |
| SEI/USDT:USDT | below_1h_threshold | +0.63% | +0.74% |
| PI/USDT:USDT | below_1h_threshold | +0.62% | +0.73% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
