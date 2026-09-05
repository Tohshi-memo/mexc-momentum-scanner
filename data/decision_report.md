# Decision Report

- generated_at: 2026-09-05T07:51:43.026940+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13707**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=13707, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.28%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.28% | **-1.28%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 8/20 | 40.0% | +3.70% | **+1.48%** |
| LIMIT_6PCT | 8/20 | 40.0% | +2.71% | **+1.08%** |
| LIMIT_9PCT | 5/20 | 25.0% | +3.20% | **+0.80%** |
| LIMIT_8PCT | 5/20 | 25.0% | +3.20% | **+0.80%** |
| LIMIT_10PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT_LONG | 10/20 | 50.0% | +1.23% | **+0.62%** |
| MARKET_LONG | 20/20 | 100.0% | +0.08% | **+0.08%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +0.17% | **+0.07%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | -0.07% | **-0.04%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | -0.06% | **-0.06%** |

## 2. $100 Live Portfolio

- 残高: **$120.56** / 初期 $100.00 (+20.56%)
- 確定トレード: 203件 (TP 75 / SL 123 / EXP 5)
- 最新: NIULAI/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.56
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$858.36** / 初期 $100.00 (+758.36%)
- 確定: 5017件 (Win 1517 / Loss 1645 / Flat 1855) / skip 5251件
- 成長率目線: 平均log +0.000429 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_7PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: MAGMA/USDT:USDT `LIMIT_7PCT` EXPIRED account +0.00% 残高後 $858.36

## 4. Robust Adaptive DryRun ($100)

- 残高: **$188.58** / 初期 $100.00 (+88.58%)
- 確定: 2454件 (Win 692 / Loss 585 / Flat 1177) / skip 4664件
- 成長率目線: 平均log +0.000258 / 幾何平均 +0.026% per trade / maxDD +3.96%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0726 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: TUT/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $188.58

## 5. Causal Adaptive DryRun ($100)

- 残高: **$118.43** / 初期 $100.00 (+18.43%)
- 確定: 2338件 (Win 699 / Loss 898 / Flat 741) / pending 6件 / skip 2842件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_7PCT` (selected_by_causal_log_growth) / causal_score +0.000271 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: TUT/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.26% 残高後 $118.43

## 6. Latest Market Context

- 更新: 2026-09-05T07:51:21.815643+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.10% price=79685.6
- Funnel: target 1050 → liquid 159 → pre 50 → checked 50 → surge 5 → strict 4
- Surge前reject: below_1h_threshold=45, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 67.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BULLA/USDT:USDT | +125.02% | $8,835,077.98 |
| 4/USDT:USDT | +75.67% | $16,639,200.66 |
| B/USDT:USDT | +53.27% | $1,925,621.83 |
| AKE/USDT:USDT | +30.14% | $13,332,978.19 |
| DASH/USDT:USDT | +27.43% | $47,999,201.80 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| 4/USDT:USDT | below_1h_threshold | +4.91% | +4.81% |
| BULLA/USDT:USDT | below_1h_threshold | +4.73% | +4.63% |
| NIULAI/USDT:USDT | below_1h_threshold | +4.08% | +3.97% |
| MARSCOIN/USDT:USDT | below_1h_threshold | +3.04% | +2.94% |
| CAKE/USDT:USDT | below_1h_threshold | +2.23% | +2.12% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
