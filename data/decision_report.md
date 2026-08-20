# Decision Report

- generated_at: 2026-08-20T20:21:32.033080+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12083**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=12083, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=-1.62%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.62% | **-1.62%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 7/20 | 35.0% | +3.96% | **+1.39%** |
| LIMIT_7PCT | 8/20 | 40.0% | +2.40% | **+0.96%** |
| LIMIT_6PCT | 9/20 | 45.0% | +1.94% | **+0.87%** |
| LIMIT_BB3S | 6/14 | 42.9% | +1.80% | **+0.77%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +5.10% | **+0.51%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +3.17% | **+2.54%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +2.67% | **+1.74%** |
| LIMIT_BB3S_LONG | 3/6 | 50.0% | +3.29% | **+1.65%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +2.74% | **+1.64%** |
| LIMIT_4PCT_LONG | 8/20 | 40.0% | +3.50% | **+1.40%** |

## 2. $100 Live Portfolio

- 残高: **$121.29** / 初期 $100.00 (+21.29%)
- 確定トレード: 188件 (TP 72 / SL 111 / EXP 5)
- 最新: VELVET/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.29
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$621.23** / 初期 $100.00 (+521.23%)
- 確定: 4296件 (Win 1314 / Loss 1404 / Flat 1578) / skip 4348件
- 成長率目線: 平均log +0.000425 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CATE/USDT:USDT `LIMIT_1PCT_LONG` TP_HIT account +1.00% 残高後 $621.23

## 4. Robust Adaptive DryRun ($100)

- 残高: **$154.16** / 初期 $100.00 (+54.16%)
- 確定: 1822件 (Win 502 / Loss 429 / Flat 891) / skip 3672件
- 成長率目線: 平均log +0.000238 / 幾何平均 +0.024% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0938 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ACE/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $154.16

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.66** / 初期 $100.00 (+16.66%)
- 確定: 1775件 (Win 527 / Loss 676 / Flat 572) / pending 6件 / skip 1777件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000189 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: CATE/USDT:USDT `LIMIT_7PCT` SL_HIT account -0.17% 残高後 $116.66

## 6. Latest Market Context

- 更新: 2026-08-20T20:21:19.075200+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.01% price=72662.7
- Funnel: target 1011 → liquid 198 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 90.2 >= 65=1, 4h RSI 80.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CATE/USDT:USDT | +51.93% | $2,467,781.12 |
| ONG/USDT:USDT | +42.02% | $6,293,215.36 |
| PEOPLE/USDT:USDT | +15.48% | $2,659,203.55 |
| TUT/USDT:USDT | +12.87% | $5,105,687.82 |
| ENA/USDT:USDT | +7.23% | $30,783,458.34 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BLESS/USDT:USDT | below_1h_threshold | +4.38% | +4.37% |
| MVLL/USDT:USDT | below_1h_threshold | +3.56% | +3.55% |
| MUU/USDT:USDT | below_1h_threshold | +3.38% | +3.36% |
| CRV/USDT:USDT | below_1h_threshold | +3.25% | +3.24% |
| RCATSTOCK/USDT:USDT | below_1h_threshold | +2.82% | +2.81% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
