# Decision Report

- generated_at: 2026-09-02T17:21:39.980664+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13354**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=13354, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.00%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.00% | **-1.00%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 5/20 | 25.0% | +5.92% | **+1.48%** |
| LIMIT_8PCT | 4/20 | 20.0% | +6.93% | **+1.39%** |
| LIMIT_9PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_6PCT | 7/20 | 35.0% | +1.92% | **+0.67%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | -0.04% | **-0.01%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 8/8 | 100.0% | +3.81% | **+3.81%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +2.53% | **+2.27%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +2.32% | **+1.62%** |
| LIMIT_4PCT_LONG | 9/20 | 45.0% | +2.67% | **+1.20%** |
| LIMIT_FIB1272_LONG | 5/20 | 25.0% | +4.26% | **+1.06%** |

## 2. $100 Live Portfolio

- 残高: **$120.80** / 初期 $100.00 (+20.80%)
- 確定トレード: 198件 (TP 74 / SL 119 / EXP 5)
- 最新: FONE/USDT:USDT TP_HIT PnL +8.00% 残高後 $120.80
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$869.23** / 初期 $100.00 (+769.23%)
- 確定: 4980件 (Win 1510 / Loss 1631 / Flat 1839) / skip 4935件
- 成長率目線: 平均log +0.000434 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: HEMI/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.63% 残高後 $869.23

## 4. Robust Adaptive DryRun ($100)

- 残高: **$181.10** / 初期 $100.00 (+81.10%)
- 確定: 2333件 (Win 655 / Loss 559 / Flat 1119) / skip 4432件
- 成長率目線: 平均log +0.000255 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1247 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: HEMI/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.43% 残高後 $181.10

## 5. Causal Adaptive DryRun ($100)

- 残高: **$114.78** / 初期 $100.00 (+14.78%)
- 確定: 2093件 (Win 611 / Loss 819 / Flat 663) / pending 0件 / skip 2737件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000336 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: CASHCAT/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $114.78

## 6. Latest Market Context

- 更新: 2026-09-02T17:21:28.268607+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.22% price=76961.6
- Funnel: target 1044 → liquid 163 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 84.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AKE/USDT:USDT | +32.21% | $20,399,386.90 |
| NIULAI/USDT:USDT | +8.57% | $2,452,393.47 |
| MARSCOIN/USDT:USDT | +8.37% | $3,178,887.86 |
| HEMI/USDT:USDT | +8.14% | $5,276,728.87 |
| BULLA/USDT:USDT | +6.05% | $1,742,821.93 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| MARSCOIN/USDT:USDT | below_1h_threshold | +4.30% | +4.52% |
| BTR/USDT:USDT | below_1h_threshold | +2.70% | +2.92% |
| BLESS/USDT:USDT | below_1h_threshold | +1.67% | +1.89% |
| BULLA/USDT:USDT | below_1h_threshold | +1.51% | +1.73% |
| NIULAI/USDT:USDT | below_1h_threshold | +1.49% | +1.71% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
