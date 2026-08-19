# Decision Report

- generated_at: 2026-08-19T07:01:45.421878+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11957**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=11957, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=-0.15%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.15% | **-0.15%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 7/20 | 35.0% | +2.79% | **+0.98%** |
| LIMIT_5PCT | 8/20 | 40.0% | +1.21% | **+0.49%** |
| LIMIT_7PCT | 4/20 | 20.0% | +2.40% | **+0.48%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +1.39% | **+0.42%** |
| LIMIT_4PCT | 13/20 | 65.0% | -0.00% | **-0.00%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 14/20 | 70.0% | +1.18% | **+0.83%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +0.89% | **+0.72%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +0.61% | **+0.42%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +1.14% | **+0.40%** |
| MARKET_LONG | 20/20 | 100.0% | +0.40% | **+0.40%** |

## 2. $100 Live Portfolio

- 残高: **$121.29** / 初期 $100.00 (+21.29%)
- 確定トレード: 188件 (TP 72 / SL 111 / EXP 5)
- 最新: VELVET/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.29
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$617.73** / 初期 $100.00 (+517.73%)
- 確定: 4218件 (Win 1297 / Loss 1377 / Flat 1544) / skip 4300件
- 成長率目線: 平均log +0.000432 / 幾何平均 +0.043% per trade / maxDD +8.13%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ACE/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $617.73

## 4. Robust Adaptive DryRun ($100)

- 残高: **$154.70** / 初期 $100.00 (+54.70%)
- 確定: 1821件 (Win 502 / Loss 428 / Flat 891) / skip 3547件
- 成長率目線: 平均log +0.000240 / 幾何平均 +0.024% per trade / maxDD +3.96%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0333 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: UNITREE/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.35% 残高後 $154.70

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.90** / 初期 $100.00 (+17.90%)
- 確定: 1735件 (Win 518 / Loss 661 / Flat 556) / pending 5件 / skip 1691件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_8PCT` (selected_by_causal_log_growth) / causal_score +0.000154 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ACE/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $117.90

## 6. Latest Market Context

- 更新: 2026-08-19T07:01:25.399534+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.02% price=64300.0
- Funnel: target 992 → liquid 176 → pre 50 → checked 50 → surge 4 → strict 4
- Surge前reject: below_1h_threshold=46, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BTW/USDT:USDT | +54.75% | $54,417,995.93 |
| HEMI/USDT:USDT | +35.58% | $1,826,235.92 |
| UNITREE/USDT:USDT | +20.34% | $12,692,680.14 |
| US/USDT:USDT | +10.74% | $1,125,790.29 |
| PUMPFUN/USDT:USDT | +6.63% | $36,480,912.01 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| DRAM/USDT:USDT | below_1h_threshold | +3.78% | +3.80% |
| EWY/USDT:USDT | below_1h_threshold | +2.72% | +2.74% |
| SAMSUNGSTOCK/USDT:USDT | below_1h_threshold | +2.69% | +2.72% |
| ACE/USDT:USDT | below_1h_threshold | +1.00% | +1.03% |
| BTW/USDT:USDT | below_1h_threshold | +0.62% | +0.65% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
