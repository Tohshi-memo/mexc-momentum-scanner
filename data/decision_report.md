# Decision Report

- generated_at: 2026-08-21T02:21:21.807850+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12125**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=12125, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=-1.21%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.21% | **-1.21%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 6/20 | 30.0% | +5.14% | **+1.54%** |
| LIMIT_3PCT | 18/20 | 90.0% | +1.02% | **+0.91%** |
| LIMIT_BB3S | 2/19 | 10.5% | +8.00% | **+0.84%** |
| LIMIT_ATR | 14/20 | 70.0% | +0.87% | **+0.61%** |
| LIMIT_10PCT | 3/20 | 15.0% | +3.15% | **+0.47%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +3.63% | **+1.81%** |
| LIMIT_5PCT_LONG | 8/20 | 40.0% | +2.77% | **+1.11%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +1.26% | **+1.01%** |
| LIMIT_ATR_LONG | 8/20 | 40.0% | +2.10% | **+0.84%** |
| LIMIT_FIB1272_LONG | 3/20 | 15.0% | +5.12% | **+0.77%** |

## 2. $100 Live Portfolio

- 残高: **$121.29** / 初期 $100.00 (+21.29%)
- 確定トレード: 188件 (TP 72 / SL 111 / EXP 5)
- 最新: VELVET/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.29
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$661.63** / 初期 $100.00 (+561.63%)
- 確定: 4336件 (Win 1332 / Loss 1420 / Flat 1584) / skip 4350件
- 成長率目線: 平均log +0.000436 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CATE/USDT:USDT `LIMIT_1PCT_LONG` TP_HIT account +1.00% 残高後 $661.63

## 4. Robust Adaptive DryRun ($100)

- 残高: **$154.16** / 初期 $100.00 (+54.16%)
- 確定: 1822件 (Win 502 / Loss 429 / Flat 891) / skip 3714件
- 成長率目線: 平均log +0.000238 / 幾何平均 +0.024% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1179 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ACE/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $154.16

## 5. Causal Adaptive DryRun ($100)

- 残高: **$118.06** / 初期 $100.00 (+18.06%)
- 確定: 1810件 (Win 537 / Loss 683 / Flat 590) / pending 4件 / skip 1783件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000204 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: CATE/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $118.06

## 6. Latest Market Context

- 更新: 2026-08-21T02:21:12.848421+00:00 / 保存件数 288/288
- BTC: BEARISH 1h -0.52% price=74709.7
- Funnel: target 1011 → liquid 192 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 87.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CATE/USDT:USDT | +89.43% | $3,993,695.44 |
| ONG/USDT:USDT | +76.38% | $29,051,222.95 |
| ONT/USDT:USDT | +21.54% | $3,469,386.68 |
| ENA/USDT:USDT | +19.14% | $52,368,206.90 |
| PEOPLE/USDT:USDT | +13.21% | $4,334,888.74 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CHIP/USDT:USDT | below_1h_threshold | +4.54% | +5.07% |
| EYE/USDT:USDT | below_1h_threshold | +4.08% | +4.60% |
| ONG/USDT:USDT | below_1h_threshold | +3.31% | +3.83% |
| PUMPFUN/USDT:USDT | below_1h_threshold | +3.03% | +3.56% |
| SAMSUNGSTOCK/USDT:USDT | below_1h_threshold | +2.73% | +3.25% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
