# Decision Report

- generated_at: 2026-08-21T03:01:32.714275+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12134**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=12134, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=-1.81%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.81% | **-1.81%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 6/20 | 30.0% | +3.95% | **+1.19%** |
| LIMIT_BB3S | 2/19 | 10.5% | +8.00% | **+0.84%** |
| LIMIT_8PCT | 5/20 | 25.0% | +3.20% | **+0.80%** |
| LIMIT_9PCT | 5/20 | 25.0% | +3.20% | **+0.80%** |
| LIMIT_ATR | 14/20 | 70.0% | +1.00% | **+0.70%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +5.12% | **+2.81%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +2.70% | **+1.48%** |
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +3.26% | **+1.47%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +1.54% | **+1.46%** |
| LIMIT_ATR_LONG | 9/20 | 45.0% | +2.67% | **+1.20%** |

## 2. $100 Live Portfolio

- 残高: **$121.29** / 初期 $100.00 (+21.29%)
- 確定トレード: 188件 (TP 72 / SL 111 / EXP 5)
- 最新: VELVET/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.29
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$666.56** / 初期 $100.00 (+566.56%)
- 確定: 4345件 (Win 1336 / Loss 1425 / Flat 1584) / skip 4350件
- 成長率目線: 平均log +0.000437 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: EYE/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $666.56

## 4. Robust Adaptive DryRun ($100)

- 残高: **$154.16** / 初期 $100.00 (+54.16%)
- 確定: 1822件 (Win 502 / Loss 429 / Flat 891) / skip 3723件
- 成長率目線: 平均log +0.000238 / 幾何平均 +0.024% per trade / maxDD +3.96%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0817 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ACE/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $154.16

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.83** / 初期 $100.00 (+17.83%)
- 確定: 1819件 (Win 540 / Loss 688 / Flat 591) / pending 5件 / skip 1784件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000175 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: EYE/USDT:USDT `MARKET_LONG` SL_HIT account -0.17% 残高後 $117.83

## 6. Latest Market Context

- 更新: 2026-08-21T03:01:22.338403+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.03% price=74390.7
- Funnel: target 1011 → liquid 194 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ONG/USDT:USDT | +95.78% | $32,060,009.63 |
| CATE/USDT:USDT | +92.44% | $4,323,953.98 |
| ONT/USDT:USDT | +26.19% | $3,599,801.75 |
| ENA/USDT:USDT | +20.82% | $53,315,166.17 |
| PEOPLE/USDT:USDT | +15.01% | $4,371,699.37 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CATE/USDT:USDT | below_1h_threshold | +2.73% | +2.76% |
| KORU/USDT:USDT | below_1h_threshold | +2.02% | +2.05% |
| MVLL/USDT:USDT | below_1h_threshold | +1.78% | +1.81% |
| SKHYNIXSTOCK/USDT:USDT | below_1h_threshold | +1.18% | +1.21% |
| AAOISTOCK/USDT:USDT | below_1h_threshold | +1.14% | +1.17% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
