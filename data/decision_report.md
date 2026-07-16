# Decision Report

- generated_at: 2026-07-16T18:11:20.830853+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8816**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=8816, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.68%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.68% | **-0.68%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 9/20 | 45.0% | +1.73% | **+0.78%** |
| LIMIT_6PCT | 7/20 | 35.0% | +1.05% | **+0.37%** |
| LIMIT_7PCT | 5/20 | 25.0% | +1.44% | **+0.36%** |
| LIMIT_5PCT | 12/20 | 60.0% | +0.53% | **+0.32%** |
| LIMIT_8PCT | 3/20 | 15.0% | +1.14% | **+0.17%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.89% | **+1.89%** |
| LIMIT_8PCT_LONG | 4/20 | 20.0% | +4.42% | **+0.88%** |
| LIMIT_7PCT_LONG | 6/20 | 30.0% | +2.82% | **+0.85%** |
| LIMIT_1PCT_LONG | 13/20 | 65.0% | +1.13% | **+0.74%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +1.07% | **+0.64%** |

## 2. $100 Live Portfolio

- 残高: **$109.89** / 初期 $100.00 (+9.89%)
- 確定トレード: 107件 (TP 40 / SL 64 / EXP 3)
- 最新: ALLO/USDT:USDT EXPIRED PnL +6.44% 残高後 $109.89
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$342.03** / 初期 $100.00 (+242.03%)
- 確定: 2931件 (Win 915 / Loss 945 / Flat 1071) / skip 2446件
- 成長率目線: 平均log +0.000420 / 幾何平均 +0.042% per trade / maxDD +8.13%
- 次の候補: `LIMIT_6PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CRO/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $342.03

## 4. Robust Adaptive DryRun ($100)

- 残高: **$107.06** / 初期 $100.00 (+7.06%)
- 確定: 778件 (Win 181 / Loss 171 / Flat 426) / skip 1449件
- 成長率目線: 平均log +0.000088 / 幾何平均 +0.009% per trade / maxDD +3.89%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0611 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: CRO/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $107.06

## 5. Causal Adaptive DryRun ($100)

- 残高: **$96.92** / 初期 $100.00 (-3.08%)
- 確定: 85件 (Win 23 / Loss 58 / Flat 4) / pending 4件 / skip 200件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000191 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: CRO/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $96.92

## 6. Latest Market Context

- 更新: 2026-07-16T18:11:11.853231+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.17% price=64155.8
- Funnel: target 880 → liquid 170 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CRO/USDT:USDT | +13.16% | $1,898,459.26 |
| TAC/USDT:USDT | +12.17% | $1,339,385.48 |
| AKE/USDT:USDT | +7.24% | $38,122,700.13 |
| ESPORTS/USDT:USDT | +6.56% | $12,127,203.37 |
| SKYAI/USDT:USDT | +5.64% | $3,296,034.76 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CRO/USDT:USDT | below_1h_threshold | +4.52% | +4.35% |
| SLX/USDT:USDT | below_1h_threshold | +1.26% | +1.08% |
| XPL/USDT:USDT | below_1h_threshold | +1.03% | +0.86% |
| DODO/USDT:USDT | below_1h_threshold | +1.03% | +0.86% |
| MYX/USDT:USDT | below_1h_threshold | +0.98% | +0.81% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
