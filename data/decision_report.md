# Decision Report

- generated_at: 2026-08-20T19:11:20.726427+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12072**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=12072, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=-0.39%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.39% | **-0.39%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 6/20 | 30.0% | +3.40% | **+1.02%** |
| LIMIT_8PCT | 4/20 | 20.0% | +5.00% | **+1.00%** |
| LIMIT_6PCT | 7/20 | 35.0% | +1.92% | **+0.67%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +5.10% | **+0.51%** |
| LIMIT_10PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +2.41% | **+1.81%** |
| MARKET_LONG | 20/20 | 100.0% | +0.99% | **+0.99%** |
| LIMIT_BB3S_LONG | 6/10 | 60.0% | +0.85% | **+0.51%** |
| LIMIT_2PCT_LONG | 10/20 | 50.0% | +0.42% | **+0.21%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +1.10% | **+0.11%** |

## 2. $100 Live Portfolio

- 残高: **$121.29** / 初期 $100.00 (+21.29%)
- 確定トレード: 188件 (TP 72 / SL 111 / EXP 5)
- 最新: VELVET/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.29
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$603.89** / 初期 $100.00 (+503.89%)
- 確定: 4285件 (Win 1309 / Loss 1400 / Flat 1576) / skip 4348件
- 成長率目線: 平均log +0.000420 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BEAT/USDT:USDT `LIMIT_ATR_LONG` SL_HIT account -0.50% 残高後 $603.89

## 4. Robust Adaptive DryRun ($100)

- 残高: **$154.16** / 初期 $100.00 (+54.16%)
- 確定: 1822件 (Win 502 / Loss 429 / Flat 891) / skip 3661件
- 成長率目線: 平均log +0.000238 / 幾何平均 +0.024% per trade / maxDD +3.96%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score -0.0220 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ACE/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $154.16

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.60** / 初期 $100.00 (+16.60%)
- 確定: 1768件 (Win 525 / Loss 675 / Flat 568) / pending 3件 / skip 1777件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_7PCT` (selected_by_causal_log_growth) / causal_score +0.000113 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BEAT/USDT:USDT `LIMIT_7PCT` EXPIRED account +0.00% 残高後 $116.60

## 6. Latest Market Context

- 更新: 2026-08-20T19:11:12.117340+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.05% price=72438.1
- Funnel: target 1011 → liquid 198 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CATE/USDT:USDT | +32.44% | $2,094,119.92 |
| PEOPLE/USDT:USDT | +9.96% | $2,188,430.23 |
| ONG/USDT:USDT | +9.26% | $4,729,725.72 |
| ALLO/USDT:USDT | +7.67% | $4,070,400.79 |
| ENA/USDT:USDT | +7.49% | $28,171,998.13 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TURBO/USDT:USDT | below_1h_threshold | +3.06% | +3.00% |
| AKE/USDT:USDT | below_1h_threshold | +2.49% | +2.43% |
| ENA/USDT:USDT | below_1h_threshold | +2.07% | +2.02% |
| FARTCOIN/USDT:USDT | below_1h_threshold | +1.72% | +1.67% |
| MET/USDT:USDT | below_1h_threshold | +1.65% | +1.59% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
