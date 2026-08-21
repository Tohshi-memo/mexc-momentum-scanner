# Decision Report

- generated_at: 2026-08-21T02:31:27.989695+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12126**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=12126, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=-1.81%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.81% | **-1.81%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 6/20 | 30.0% | +5.14% | **+1.54%** |
| LIMIT_3PCT | 19/20 | 95.0% | +0.91% | **+0.87%** |
| LIMIT_BB3S | 2/19 | 10.5% | +8.00% | **+0.84%** |
| LIMIT_ATR | 14/20 | 70.0% | +0.87% | **+0.61%** |
| LIMIT_10PCT | 3/20 | 15.0% | +3.15% | **+0.47%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT_LONG | 9/20 | 45.0% | +4.48% | **+2.01%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +1.83% | **+1.46%** |
| LIMIT_5PCT_LONG | 7/20 | 35.0% | +3.62% | **+1.27%** |
| LIMIT_ATR_LONG | 7/20 | 35.0% | +2.86% | **+1.00%** |
| MARKET_LONG | 20/20 | 100.0% | +1.00% | **+1.00%** |

## 2. $100 Live Portfolio

- 残高: **$121.29** / 初期 $100.00 (+21.29%)
- 確定トレード: 188件 (TP 72 / SL 111 / EXP 5)
- 最新: VELVET/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.29
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$665.81** / 初期 $100.00 (+565.81%)
- 確定: 4337件 (Win 1333 / Loss 1420 / Flat 1584) / skip 4350件
- 成長率目線: 平均log +0.000437 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CATE/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.63% 残高後 $665.81

## 4. Robust Adaptive DryRun ($100)

- 残高: **$154.16** / 初期 $100.00 (+54.16%)
- 確定: 1822件 (Win 502 / Loss 429 / Flat 891) / skip 3715件
- 成長率目線: 平均log +0.000238 / 幾何平均 +0.024% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1127 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ACE/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $154.16

## 5. Causal Adaptive DryRun ($100)

- 残高: **$118.26** / 初期 $100.00 (+18.26%)
- 確定: 1811件 (Win 538 / Loss 683 / Flat 590) / pending 6件 / skip 1783件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000205 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: CATE/USDT:USDT `MARKET_LONG` EXPIRED account +0.17% 残高後 $118.26

## 6. Latest Market Context

- 更新: 2026-08-21T02:31:16.934523+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.09% price=75035.5
- Funnel: target 1011 → liquid 192 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 87.2 >= 65=1, 4h RSI 71.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CATE/USDT:USDT | +91.60% | $4,041,916.88 |
| ONG/USDT:USDT | +79.02% | $29,457,271.76 |
| ONT/USDT:USDT | +22.33% | $3,493,264.00 |
| ENA/USDT:USDT | +20.06% | $52,688,415.92 |
| PEOPLE/USDT:USDT | +14.51% | $4,362,241.46 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ONG/USDT:USDT | below_1h_threshold | +4.88% | +4.97% |
| CRV/USDT:USDT | below_1h_threshold | +4.65% | +4.74% |
| NIULAI/USDT:USDT | below_1h_threshold | +3.86% | +3.95% |
| EYE/USDT:USDT | below_1h_threshold | +3.71% | +3.80% |
| MAGMA/USDT:USDT | below_1h_threshold | +3.00% | +3.09% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
