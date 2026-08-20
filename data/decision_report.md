# Decision Report

- generated_at: 2026-08-20T20:46:52.659442+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12094**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=12094, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=-0.42%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.42% | **-0.42%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 20/20 | 100.0% | +0.59% | **+0.59%** |
| LIMIT_FIB1272 | 4/20 | 20.0% | +2.13% | **+0.43%** |
| LIMIT_2PCT | 18/20 | 90.0% | +0.32% | **+0.29%** |
| LIMIT_BB3S | 7/17 | 41.2% | +0.57% | **+0.23%** |
| LIMIT_10PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/3 | 66.7% | +2.70% | **+1.80%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +1.70% | **+1.44%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +1.20% | **+0.84%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +1.24% | **+0.80%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +1.31% | **+0.78%** |

## 2. $100 Live Portfolio

- 残高: **$121.29** / 初期 $100.00 (+21.29%)
- 確定トレード: 188件 (TP 72 / SL 111 / EXP 5)
- 最新: VELVET/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.29
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$646.58** / 初期 $100.00 (+546.58%)
- 確定: 4307件 (Win 1321 / Loss 1407 / Flat 1579) / skip 4348件
- 成長率目線: 平均log +0.000433 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AVAAI/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.63% 残高後 $646.58

## 4. Robust Adaptive DryRun ($100)

- 残高: **$154.16** / 初期 $100.00 (+54.16%)
- 確定: 1822件 (Win 502 / Loss 429 / Flat 891) / skip 3683件
- 成長率目線: 平均log +0.000238 / 幾何平均 +0.024% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1269 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ACE/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $154.16

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.37** / 初期 $100.00 (+17.37%)
- 確定: 1784件 (Win 530 / Loss 677 / Flat 577) / pending 4件 / skip 1782件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000256 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ONT/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $117.37

## 6. Latest Market Context

- 更新: 2026-08-20T20:46:31.349133+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.12% price=72738.3
- Funnel: target 1011 → liquid 200 → pre 50 → checked 50 → surge 6 → strict 2
- Surge前reject: below_1h_threshold=44, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 91.7 >= 65=1, 4h RSI 94.1 >= 65=1, 4h RSI 81.0 >= 65=1, 4h RSI 84.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ONG/USDT:USDT | +64.63% | $8,382,883.86 |
| CATE/USDT:USDT | +51.59% | $2,656,631.72 |
| ONT/USDT:USDT | +40.70% | $1,185,769.87 |
| PEOPLE/USDT:USDT | +16.07% | $2,794,373.09 |
| AVAAI/USDT:USDT | +8.37% | $1,560,229.89 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| MVLL/USDT:USDT | below_1h_threshold | +3.56% | +3.44% |
| CRV/USDT:USDT | below_1h_threshold | +3.47% | +3.36% |
| MUU/USDT:USDT | below_1h_threshold | +3.38% | +3.26% |
| RCATSTOCK/USDT:USDT | below_1h_threshold | +2.82% | +2.71% |
| COLLECT/USDT:USDT | below_1h_threshold | +2.73% | +2.62% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
