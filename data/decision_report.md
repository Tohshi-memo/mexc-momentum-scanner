# Decision Report

- generated_at: 2026-09-02T18:21:39.383939+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13360**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=13360, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=-2.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.20% | **-2.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 7/20 | 35.0% | +4.06% | **+1.42%** |
| LIMIT_8PCT | 5/20 | 25.0% | +4.74% | **+1.19%** |
| LIMIT_9PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_FIB1618 | 3/20 | 15.0% | +3.41% | **+0.51%** |
| LIMIT_6PCT | 8/20 | 40.0% | +1.18% | **+0.47%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 7/7 | 100.0% | +5.78% | **+5.78%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +2.55% | **+2.17%** |
| MARKET_LONG | 20/20 | 100.0% | +2.00% | **+2.00%** |
| LIMIT_4PCT_LONG | 7/20 | 35.0% | +4.57% | **+1.60%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +2.53% | **+1.52%** |

## 2. $100 Live Portfolio

- 残高: **$120.80** / 初期 $100.00 (+20.80%)
- 確定トレード: 198件 (TP 74 / SL 119 / EXP 5)
- 最新: FONE/USDT:USDT TP_HIT PnL +8.00% 残高後 $120.80
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$879.05** / 初期 $100.00 (+779.05%)
- 確定: 4985件 (Win 1512 / Loss 1632 / Flat 1841) / skip 4936件
- 成長率目線: 平均log +0.000436 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AKE/USDT:USDT `LIMIT_BB3S_LONG` TP_HIT account +1.00% 残高後 $879.05

## 4. Robust Adaptive DryRun ($100)

- 残高: **$181.85** / 初期 $100.00 (+81.85%)
- 確定: 2339件 (Win 657 / Loss 561 / Flat 1121) / skip 4432件
- 成長率目線: 平均log +0.000256 / 幾何平均 +0.026% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1460 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: FONE/USDT:USDT `LIMIT_1PCT_LONG` TP_HIT account +0.69% 残高後 $181.85

## 5. Causal Adaptive DryRun ($100)

- 残高: **$114.78** / 初期 $100.00 (+14.78%)
- 確定: 2093件 (Win 611 / Loss 819 / Flat 663) / pending 0件 / skip 2742件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000327 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: CASHCAT/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $114.78

## 6. Latest Market Context

- 更新: 2026-09-02T18:21:24.861241+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.07% price=77402.2
- Funnel: target 1044 → liquid 161 → pre 50 → checked 50 → surge 3 → strict 1
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 87.8 >= 65=1, 4h RSI n/a=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AKE/USDT:USDT | +51.36% | $24,051,577.37 |
| FONE/USDT:USDT | +18.03% | $1,971,481.81 |
| BULLA/USDT:USDT | +8.43% | $1,838,303.97 |
| MARSCOIN/USDT:USDT | +7.28% | $3,080,776.26 |
| HEMI/USDT:USDT | +7.15% | $5,189,677.29 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BULLA/USDT:USDT | below_1h_threshold | +3.50% | +3.43% |
| PONS/USDT:USDT | below_1h_threshold | +2.96% | +2.89% |
| BTW/USDT:USDT | below_1h_threshold | +2.10% | +2.03% |
| EGLD/USDT:USDT | below_1h_threshold | +1.74% | +1.67% |
| OP/USDT:USDT | below_1h_threshold | +1.67% | +1.60% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
