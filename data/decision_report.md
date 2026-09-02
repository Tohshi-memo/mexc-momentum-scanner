# Decision Report

- generated_at: 2026-09-02T16:46:46.475188+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13351**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=13351, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.60%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.60% | **-1.60%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 4/20 | 20.0% | +6.93% | **+1.39%** |
| LIMIT_7PCT | 5/20 | 25.0% | +4.88% | **+1.22%** |
| LIMIT_6PCT | 7/20 | 35.0% | +2.76% | **+0.97%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +1.34% | **+0.47%** |
| LIMIT_5PCT | 9/20 | 45.0% | +0.40% | **+0.18%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 6/6 | 100.0% | +4.41% | **+4.41%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +3.69% | **+3.33%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +3.59% | **+2.33%** |
| MARKET_LONG | 20/20 | 100.0% | +2.00% | **+2.00%** |
| LIMIT_ATR_LONG | 10/20 | 50.0% | +3.47% | **+1.73%** |

## 2. $100 Live Portfolio

- 残高: **$120.80** / 初期 $100.00 (+20.80%)
- 確定トレード: 198件 (TP 74 / SL 119 / EXP 5)
- 最新: FONE/USDT:USDT TP_HIT PnL +8.00% 残高後 $120.80
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$872.48** / 初期 $100.00 (+772.48%)
- 確定: 4977件 (Win 1509 / Loss 1629 / Flat 1839) / skip 4935件
- 成長率目線: 平均log +0.000435 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AKE/USDT:USDT `LIMIT_1PCT_LONG` TP_HIT account +1.00% 残高後 $872.48

## 4. Robust Adaptive DryRun ($100)

- 残高: **$181.60** / 初期 $100.00 (+81.60%)
- 確定: 2330件 (Win 654 / Loss 557 / Flat 1119) / skip 4432件
- 成長率目線: 平均log +0.000256 / 幾何平均 +0.026% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1431 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: AKE/USDT:USDT `LIMIT_1PCT_LONG` TP_HIT account +0.69% 残高後 $181.60

## 5. Causal Adaptive DryRun ($100)

- 残高: **$114.78** / 初期 $100.00 (+14.78%)
- 確定: 2093件 (Win 611 / Loss 819 / Flat 663) / pending 0件 / skip 2735件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000376 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: CASHCAT/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $114.78

## 6. Latest Market Context

- 更新: 2026-09-02T16:46:28.220362+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.03% price=77230.0
- Funnel: target 1044 → liquid 163 → pre 50 → checked 50 → surge 5 → strict 3
- Surge前reject: below_1h_threshold=45, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 81.7 >= 65=1, 4h RSI 74.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AKE/USDT:USDT | +22.26% | $17,360,530.18 |
| HEMI/USDT:USDT | +8.45% | $5,393,888.41 |
| ARB/USDT:USDT | +6.08% | $57,191,230.21 |
| MARSCOIN/USDT:USDT | +5.77% | $3,327,580.19 |
| NIULAI/USDT:USDT | +5.55% | $2,560,004.17 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| MAGMA/USDT:USDT | below_1h_threshold | +4.99% | +5.02% |
| USELESS/USDT:USDT | below_1h_threshold | +4.82% | +4.85% |
| BULLA/USDT:USDT | below_1h_threshold | +3.63% | +3.65% |
| EGLD/USDT:USDT | below_1h_threshold | +3.33% | +3.36% |
| CASHCAT/USDT:USDT | below_1h_threshold | +2.96% | +2.99% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
